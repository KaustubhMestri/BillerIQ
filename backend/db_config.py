import pyodbc
def connect_db():
    try:
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=KAUSTUBH-SWIFT5;'
            'DATABASE=Inventory_Management_System;'
            'Trusted_Connection=yes;'
            'Encrypt=no;'
        )
        print("Connection to SQL Server successfully.")
        return conn
    except Exception as e:
        print('Database Connection Failed: ', e)
        return None