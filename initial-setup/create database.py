from mysql.connector import connect

connection = connect(user="root", password="8235", host="127.0.0.1", database="library")
cursor = connection.cursor()

with open('tables.sql', 'r') as tables:
    sql = tables.read()
    commands = sql.split(';')
    for command in commands:
        cursor.execute(command)
        connection.commit()

with open('values.sql', 'r') as values:
    sql = values.read()
    commands = sql.split(';')
    for command in commands:
        cursor.execute(command)
        connection.commit()
