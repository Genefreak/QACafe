import sqlite3

connection = sqlite3.connect("drinks")
cursor = connection.cursor()


sql_file = open("drinks.sql")
sql_string = sql_file.read()
cursor.executescript(sql_string)
