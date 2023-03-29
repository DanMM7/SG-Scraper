import os 
import sys
from Connection import connect


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