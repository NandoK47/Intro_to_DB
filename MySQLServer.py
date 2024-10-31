import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',  
            user='your_username',  
            password='your_password'  
        )

        if connection.is_connected():
            cursor = connection.cursor()
            
            try:
                cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
                print("Database 'alx_book_store' created successfully!")
            except Error as e:
                print("Error creating database:", e)
            finally:
                
                cursor.close()

    except Error as e:
        print("Error connecting to MySQL server:", e)

    finally:
        
        if connection.is_connected():
            connection.close()
            print("MySQL connection closed.")


create_database()
