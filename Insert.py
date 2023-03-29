import os 
import sys
from Connection import Conn


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


# Close Connection