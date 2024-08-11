import mysql.connector
from mysql.connector import Error

def insert_user(data, info_label, info2_label):
    try:
        connection = mysql.connector.connect(
            host='your_host',
            database='your_database',
            user='your_user',
            password='your_password'
        )
        
        if connection.is_connected():
            cursor = connection.cursor()

            username = data['username']
            phone_number = data['phone_number']

            # Username unique ekanligini tekshirish
            cursor.execute("SELECT COUNT(*) FROM users WHERE username = %s", (username,))
            username_exists = cursor.fetchone()[0]

            if username_exists:
                info_label.setText("User already exists")
                return

            # Phone number unique ekanligini tekshirish
            cursor.execute("SELECT COUNT(*) FROM users WHERE phone_number = %s", (phone_number,))
            phone_number_exists = cursor.fetchone()[0]

            if phone_number_exists:
                info2_label.setText("Phone number already exists")
                return

            # Agar har ikkalasi ham unique bo'lsa, yangi foydalanuvchini qo'shish
            insert_query = "INSERT INTO users (username, password, phone_number) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (username, data['password'], phone_number))
            connection.commit()
            info_label.setText("User inserted successfully")
            info2_label.setText("")

    except Error as e:
        error_message = str(e)
        if "username" in error_message:
            info_label.setText("Error with username: " + error_message)
        elif "phone_number" in error_message:
            info2_label.setText("Error with phone number: " + error_message)
        else:
            info_label.setText("General error: " + error_message)
            info2_label.setText("General error: " + error_message)
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
