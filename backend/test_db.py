from db_config import connect_db

conn = connect_db()

if conn:
    cursor = conn.cursor()
    cursor.execute("Select GETDATE()")
    result = cursor.fetchone()
    print('Current SQL Server Time:', result[0])
    conn.close()
else:
    print('Connection could not be established.')
