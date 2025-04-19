import mysql.connector

class DatabaseConnection:
    def __init__(self):
            self.connection = mysql.connector.connect(
                host = "localhost",
                user = "root",
                passwd = "samalexis123",
                database = "ssis"
            )
            if self.connection.is_connected():
                print("Successfully connected to MySQL database")

    def get_connection(self):
        return self.connection

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("MySQL connection closed")
        
