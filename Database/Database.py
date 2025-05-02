import mysql.connector

class DatabaseConnection:
    def __init__(self):
            self.connection = mysql.connector.connect(
                host = "sql12.freesqldatabase.com",
                user = "sql12776495",
                passwd = "qnb3UyFNtS",
                database = "sql12776495"
            )
            if self.connection.is_connected():
                print("Successfully connected to MySQL database")

    def get_connection(self):
        return self.connection

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("MySQL connection closed")
        
