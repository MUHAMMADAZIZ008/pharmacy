#Bismillah
import mysql.connector
from mysql.connector import Error

class Database:
<<<<<<< HEAD
    def __init__(self) -> None:
        self.connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'Mm08gulomov',
            database = 'pharmacy'
        )
=======
    def __init__(self):
        self.connection = None 
        self.connect() 

    def connect(self):
        if self.connection is None or not self.connection.is_connected():
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="mr2344",
                database="pharmacy"
            )
>>>>>>> ef0dc176cea3748721bb6def44f8e9eab1b85ea9


    def insert_user(self, data, info_label, info2_label):
        try:
            with self.connection.cursor() as cursor:

                username = data['username']
                phone_number = data['phone_number']

                cursor.execute("SELECT COUNT(*) FROM Users_data WHERE username = %s", (username,))
                username_exists = cursor.fetchone()[0]

                if username_exists:
                    info_label.setText("User already exists")
                    return False

                cursor.execute("SELECT COUNT(*) FROM Users_data WHERE phone_number = %s", (phone_number,))
                phone_number_exists = cursor.fetchone()[0]

                if phone_number_exists:
                    info2_label.setText("Phone number already exists")
                    return False

                insert_query = "INSERT INTO Users_data (username, password, phone_number) VALUES (%s, %s, %s)"
                cursor.execute(insert_query, (username, data['password'], phone_number))
                self.connection.commit()
                info_label.setText("User inserted successfully")
                info2_label.setText("")
                return True 

        except Error as e:
            error_message = str(e)
            if "username" in error_message:
                info_label.setText("Error with username: " + error_message)
            elif "phone_number" in error_message:
                info2_label.setText("Error with phone number: " + error_message)
            else:
                info_label.setText("General error: " + error_message)
                info2_label.setText("General error: " + error_message)
            return False 

        finally:
            if self.connection.is_connected():
                cursor.close()
                self.connection.close()



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
        
# barcha dorilarni ma'lumotlari bilan olish
    
    # def Get_all_medicine_items(self):
    #     with self.connection.cursor() as cursor:
        
    #         query = 'SELECT * FROM Medicine_items'
    #         cursor.execute(query)
            
    #         rows = cursor.fetchall()
            
    #     return rows

    def Get_all_medicine_items(self):
        self.connect()  # Ulanishni tekshirish va qayta ochish
        with self.connection.cursor() as cursor:
            query = 'SELECT * FROM Medicine_items'
            cursor.execute(query)
            rows = cursor.fetchall()
        return rows
    
# dorini update qilish    

    def update_medicine(self, item: dict):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(f"""
                    UPDATE medicine_items
                    SET name = "{item['name']}", produced_time = "{item['produced_time']}", end_time = "{item['end_time']}", expiration_date = "{item['expiration_date']}", price = "{item['price']}", count = "{item['count']}"
                    WHERE id = "{item["id"]}";
                """)
            
            self.connection.commit()
            return True
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
