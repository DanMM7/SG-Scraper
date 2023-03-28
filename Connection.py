import pypyodbc as odbc
import textwrap

# Connection Strings
DATABASE_NAME = ''

connection_string = ("Driver={SQL Server Native Client 11.0};"
                     "Server=GHDEVVMSRV04;"
                     "Database=SGCadasterSystem;"
                     "Trusted_Connection=yes;"
                     "uid=sa;"
                     "pwd=s8_@dm1n;")

connect = odbc.connect(connection_string)
print(connect)



#cursor = connect.cursor()
#cursor.execute('SELECT TOP (3) *  FROM [SGCadasterSystem].[dbo].[FORM_SGDocumentPages]')

#for row in cursor:
#    print('row = %r' % (row,))


# Connect to Database

