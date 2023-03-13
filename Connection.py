""" import pyodbc
import textwrap

server = 'test-wc-server.database.windows.net'
database = 'Customers'
username = 'danzure'
password = '{adminkey@123}'   
driver= '{ODBC Driver 17 for SQL Server}'

with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT TOP (3) * FROM [dbo].[scraper_formdetails]")
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone() """

def all_students():
    qu= "SELECT [PK_ID], [DESCRIPTION] FROM [SGCadasterSystem].[dbo].[LK_SGOfficeCodes]"
    students = crs.execute(qu)
    students_data = []
    for row in students:
        student= {"ID":row[0], "Description":row[2]}
        students_data.append(student)

    final_data["students_info"] = students_data
    return final_data