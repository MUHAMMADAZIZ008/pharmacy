#Bismillah
import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self) -> None:
        self.connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'mr2344',
            database = 'pharmacy'
        )

# User qo'shish

    def insert_user(self, user: dict):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(f'''
                    INSERT INTO users_data (username, password, phone_number) 
                    VALUES ('{user['username']}','{user['password']}','{user['phone_number']}')
                ''')
                self.connection.commit()
                return False
        except Error as err:
            return str(err)


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
    
    def Get_all_medicine_items(self):
        with self.connection.cursor() as cursor:
        
            query = 'SELECT * FROM Medicine_items'
            cursor.execute(query)
            
            rows = cursor.fetchall()
            
        return rows
    
# dorini update qilish    

    def update_medicine(self, item: dict):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("""
                UPDATE Medicine_items
                SET name = %s, produced_time = %s, end_time = %s, expiration_date, = %s, price = %s, count = %s
                WHERE id = %s;
                """,
                (item['id'], item['name'], item['produced_time'], item['end_time'], item['expiration_date'], item['price'], item['count'] ))
            
            self.connection.commit()
            return None
        except Error as err:

            self.connection.rollback()
            return str(err)