import mysql.connector
from mysql.connector import Error
from datetime import datetime
class Database:
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        if self.connection is None or not self.connection.is_connected():
            try:
                self.connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="mr2344",
                    database="pharmacy"
                )
                self.cursor = self.connection.cursor(buffered=True)
            except Error as err:
                print(f"Error: {err}")
                self.connection = None
                self.cursor = None

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection and self.connection.is_connected():
            self.connection.close()

    def is_username_exists(self, username):
        query = "SELECT COUNT(*) FROM Users_data WHERE username = %s"
        self.cursor.execute(query, (username,))
        result = self.cursor.fetchone()
        return result[0] > 0

    def is_phone_number_exists(self, phone_number):
        query = "SELECT COUNT(*) FROM Users_data WHERE phone_number = %s"
        self.cursor.execute(query, (phone_number,))
        result = self.cursor.fetchone()
        return result[0] > 0

    def insert_user(self, user):
        try:
            query = "INSERT INTO Users_data (username, password, phone_number) VALUES (%s, %s, %s)"
            self.cursor.execute(query, (user['username'], user['password'], user['phone_number']))
            self.connection.commit()
            return True
        except Error as e:
            print(f"Error inserting user: {e}")
            return False


# bitta userni ma'lumotlarini olish va yuborish

    def get_user_data(self, user: dict):
        try:
            with self.connection.cursor() as cursor:
                query = '''
                    SELECT * FROM Users_data WHERE username = %s AND password = %s
                '''
                cursor.execute(query, (user['login'], user['password']))
                self.all_data = cursor.fetchall()
                return self.all_data
        except Error as err:
            return str(err)

# bitta admin ma'lumotlarini olish va yuborish   

    def get_admin_data(self, admin: dict):
        try:
            with self.connection.cursor() as cursor:
                query = '''
                    SELECT * FROM Admins_data WHERE username = %s AND password = %s
                '''
                cursor.execute(query, (admin['login'], admin['password']))
                self.all_data = cursor.fetchall()
                return self.all_data
        except Error as err:
            return str(err)

#yangi dori qo'shish

    def insert_Medicine(self, item: dict):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(f'''
                    INSERT INTO Medicine_items (name, produced_time, end_time, expiration_date, price, count) 
                    VALUES ('{item['name']}','{item['produced_time']}','{item['end_time']}', '{item['expiration_date']}', '{item['price']}', '{item['count']}')
                ''')
                self.connection.commit()
                return False
        except Error as err:
            return str(err)

# dorini o'chirib tashlash

    def delete_medicine_item(self, item: dict):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("""
                DELETE FROM Medicine_items
                WHERE id = %s;
                """,
                ( item['id'],))
            self.connection.commit()
            return None 
        except Error as err:

            self.connection.rollback()
            return str(err)
        

    def Get_all_medicine_items(self):
        self.connect()  
        with self.connection.cursor() as cursor:
            query = 'SELECT * FROM Medicine_items'
            cursor.execute(query)
            rows = cursor.fetchall()
        return rows
    
# dorini update qilish    


    def update_medicine(self, item: dict):
        try:
            with self.connection.cursor() as cursor:

                cursor.execute("SELECT COUNT(*) FROM medicine_items WHERE id = %s", (item["id"],))
                if cursor.fetchone()[0] == 0:
                    return 0 

                cursor.execute("""
                    UPDATE medicine_items
                    SET name = %s, produced_time = %s, end_time = %s, expiration_date = %s, price = %s, count = %s
                    WHERE id = %s
                """, (item['name'], item['produced_time'], item['end_time'], item['expiration_date'], item['price'], item['count'], item["id"]))

            self.connection.commit()
            return 1 
        except Error as err:
            self.connection.rollback()
            return str(err)


    def update_tabele(self, item: dict):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("""
                UPDATE medicine_items
                SET name = %s, produced_time = %s, end_time = %s, expiration_date, = %s, price = %s
                """,
                ( item['name'], item['produced_time'], item['end_time'], item['expiration_date'], item['price'] ))
            
            self.connection.commit()
            return None
        except Error as err:

            self.connection.rollback()
            return str(err)


    def calculate_expiration_date(self, produced_time, end_time):
        try:
            produced_date = datetime.strptime(produced_time, '%Y-%m-%d')
            end_date = datetime.strptime(end_time, '%Y-%m-%d')
            expiration_date = end_date.year - produced_date.year
            if (end_date.month, end_date.day) < (produced_date.month, produced_date.day):
                expiration_date -= 1
            return expiration_date
        except ValueError:
            return None

    def insert_product(self, data):
        expiration_date = self.calculate_expiration_date(data['produced_time'], data['end_time'])
        if expiration_date is None:
            return "Error: Invalid date format. Use yyyy-mm-dd."

        if self.connection is None:
            return "Error: No connection to the database."

        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM Medicine_items WHERE name = %s", (data['name'],))
                product_exists = cursor.fetchone()[0]

                if product_exists:
                    return "Error: Product already exists"

                insert_query = """
                INSERT INTO Medicine_items (name, produced_time, end_time, expiration_date, price, count)
                VALUES (%s, %s, %s, %s, %s, %s)
                """
                cursor.execute(insert_query, (data['name'], data['produced_time'], data['end_time'], expiration_date, data['price'], data['count']))
                self.connection.commit()
                return "Product added successfully"

        except Error as e:
            error_message = str(e)
            return f"Error: {error_message}"

        finally:
            if self.connection.is_connected():
                self.connection.close()

# O'zgartirib arxivga saqlab ketadi

    def delete_medicine(self, medicine_id):
        try:
            with self.connection.cursor() as cursor:

                cursor.execute("SELECT * FROM Medicine_items WHERE id = %s", (medicine_id,))
                medicine = cursor.fetchone()

                if medicine:

                    insert_query = """
                        INSERT INTO Arxiv_items (id, name, produced_time, end_time, expiration_date, price, count)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """
                    cursor.execute(insert_query, medicine)

                    delete_query = "DELETE FROM Medicine_items WHERE id = %s"
                    cursor.execute(delete_query, (medicine_id,))
                    self.connection.commit()
                    return True
                else:
                    return "Mahsulot topilmadi."

        except Exception as e:
            return str(e)


    def Get_all_users_data(self):
        with self.connection.cursor() as cursor:
            query = 'SELECT * FROM medicine_items'
            cursor.execute(query)
            
            rows = cursor.fetchall()
            
        return rows

    def delete_user_data(self, user: dict):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("""
                DELETE FROM medicine_items
                WHERE name = %s;
                """,
                ( user['name'],))
            self.connection.commit()
            return None
        except Error as err:
            self.connection.rollback()
            return str(err)
