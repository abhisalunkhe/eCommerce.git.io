#!C:\\Users\\del\\anaconda3\\python.exe

print("Content-type:text/html; charset=utf-0\n\n")

import cgitb,cgi
import MySQLdb

cgitb.enable()

form = cgi.FieldStorage()
email = form.getvalue("email")

connection = MySQLdb.connect('localhost','root','','ecommerce')

cursor = connection.cursor()
cursor.execute("insert into subscribe values('%s')"%(email))
print("Subscribed")
connection.commit()
connection.close()
