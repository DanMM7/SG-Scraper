import pypyodbc as odbc
import textwrap


# Write to FORM_OfficeLog Table if you get Java.sql.SQLException or Webpage Crash error
def SGOfficeCodeResult(connect):
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM [SGCadasterSystem].[dbo].[LK_SGOfficeCodes] WHERE [SGOfficeUnitCode] IS NOT NULL AND PK_ID IN (1,2,8) ')
    rows = cursor.fetchall()




# Write to FORM_OfficeLog Table if you get Java.sql.SQLException or Webpage Crash error
def OfficeOfflineLog(connect):
    cursor = connect.cursor()
    #cursor.execute('INSERT INTO [SGCadasterSystem].[dbo].[FORM_OfficeOfflineLog] ([OfficeKey]) VALUES(?)')



# Write to FORM_SGDocuments if Data for Web is > 1
def SGDocument(connect):
    cursor = connect.cursor()
    #cursor.execute('INSERT INTO [SGCadasterSystem].[dbo].[FORM_SGDocuments] ([DocumentNumber], SGOffice) VALUES([DocNr], [sgOfficeCode]) SELECT @@IDENTITY')



# Write to FORM_SGDocuments if Data for Web is > 1
def SGDocumentPages(connect):
    cursor = connect.cursor()
    #cursor.execute('INSERT INTO [SGCadasterSystem].[dbo].[FORM_SGDocumentPages] (DocumentID, DocumentLink, [PageNumber], [PageType]) VALUES([DocNr], LTRIM(3, 1, 2)')




#Main function 
if __name__ == '__main__':

    # Connection Strings
    connection_string = ("Driver={SQL Server};"
                         "Server=GIDEVVMSRV04;"
                         "Database=SGCadasterSystem;"
                         "Trusted_Connection=no;"
                         "uid=sa;"
                         "pwd=s8_@dm1n;")


    # Connect to Database
    connect = odbc.connect(connection_string)

    OfficeOfflineLog(connect)
    SGDocument(connect)
    SGDocumentPages(connect)
