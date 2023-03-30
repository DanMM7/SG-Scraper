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


# Display Fetch Office Codes from LK_SGOfficeCodes Table
def SGOfficeCodeResult():
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM [SGCadasterSystem].[dbo].[LK_SGOfficeCodes] WHERE [SGOfficeUnitCode] IS NOT NULL AND PK_ID IN (1,2,8);')

    for row in cursor:
        print('row = %r' % (row,))


# Display Fetch Office Codes from LK_SGOfficeCodes Table
def MissingDocuments():
    office_codes = connect.cursor()
    cursor.execute('SELECT * FROM [SGCadasterSystem].[dbo].[vw_MissingDocuments] WHERE [SGOfficeCode] = [PK_ID]')

    for row in office_codes:
        print('row = %r' % (row,))


# Display Fetch Office Codes from LK_SGOfficeCodes Table
def Display_SGDocument():
    office_codes = connect.cursor()
    cursor.execute('SELECT COUNT(*) FROM [SGCadasterSystem].[dbo].[FORM_SGDocuments] WHERE [DocumentNumber] = [PK_ID] AND SGOffice=SGOfficeCode')

    for row in office_codes:
        print('row = %r' % (row,))


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


# Write to FORM_OfficeLog Table if you get Java.sql.SQLException error
def OfficeOfflineLog():
    office_codes = connect.cursor()
    cursor.execute('INSERT INTO [SGCadasterSystem].[dbo].[FORM_OfficeOfflineLog] ([OfficeKey]) VALUES([PK_ID])')

    for row in office_codes:
        print('row = %r' % (row,))

# Write to FORM_OfficeLog Table if you get Error error
def OfficeOfflineLog2():
    office_codes = connect.cursor()
    cursor.execute('INSERT INTO [SGCadasterSystem].[dbo].[FORM_OfficeOfflineLog] ([OfficeKey]) VALUES([PK_ID])')

    for row in office_codes:
        print('row = %r' % (row,))

# Write to FORM_SGDocuments if Data for Web is > 1
def SGDocument():
    office_codes = connect.cursor()
    cursor.execute('INSERT INTO [SGCadasterSystem].[dbo].[FORM_SGDocuments] ([DocumentNumber], SGOffice) VALUES([DocNr], [sgOfficeCode]) SELECT @@IDENTITY')

    for row in office_codes:
        print('row = %r' % (row,))

# Write to FORM_SGDocuments if Data for Web is > 1
def SGDocumentPages():
    office_codes = connect.cursor()
    cursor.execute('INSERT INTO [SGCadasterSystem].[dbo].[FORM_SGDocumentPages] (DocumentID, DocumentLink, [PageNumber], [PageType]) VALUES([DocNr], LTRIM(3, 1, 2)')

    for row in office_codes:
        print('row = %r' % (row,))



