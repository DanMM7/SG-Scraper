import pypyodbc as odbc
import textwrap

# Connection Strings
DATABASE_NAME = ''

connection_string = ("Driver={SQL Server};"
                     "Server=GIDEVVMSRV04;"
                     "Database=SGCadasterSystem;"
                     "Trusted_Connection=no;"
                     "uid=sa;"
                     "pwd=s8_@dm1n;")


# Connect to Database
connect = odbc.connect(connection_string)
print(connect)


# Run test query
cursor = connect.cursor()
cursor.execute('SELECT TOP (3) *  FROM [SGCadasterSystem].[dbo].[FORM_SGDocumentPages]')

for row in cursor:
    print('row = %r' % (row,))



