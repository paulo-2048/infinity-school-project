# Username: S8Pm8DjSMe

# Database name: S8Pm8DjSMe

# Password: iLtme9GwPN

# Server: remotemysql.com

# Port: 3306

# SalesRow
#######################################################

import mysql.connector
from mysql.connector import Error


class Connection:
    def __init__(self):
        pass

    def connectdb(self):
        try:
            user = 'S8Pm8DjSMe'
            database = 'S8Pm8DjSMe'
            password = 'iLtme9GwPN'
            host = 'remotemysql.com'
            self.con = mysql.connector.connect(
                host=host, password=password, user=user, database=database)
            if self.con.is_connected():
                return True
            else:
                return False
        except Error as e:
            print(e)
            return False
