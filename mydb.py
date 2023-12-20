import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '234765890@Pgrs',

)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE dcrm")

print ("All DONE!")