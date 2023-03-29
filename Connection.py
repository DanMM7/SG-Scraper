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


""" Run test query
    print(connect)
    cursor = connect.cursor()
    cursor.execute('SELECT TOP (3) *  FROM [SGCadasterSystem].[dbo].[FORM_SGDocumentPages]')

    for row in cursor:
        print('row = %r' % (row,))

    cursor = connect.cursor()
    cursor.execute('SELECT * FROM [SGCadasterSystem].[dbo].[LK_SGOfficeCodes] WHERE [SGOfficeUnitCode] IS NOT NULL AND PK_ID IN (1,2,8);')

    for row in cursor:
        print('row = %r' % (row,))"""


