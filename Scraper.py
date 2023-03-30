import pandas as pd
import jpype
from functools import reduce
import requests
from bs4 import BeautifulSoup
import pypyodbc as odbc
import Connection as Conn




def ScapePage(url):

    for office in range(1, 11):
        for key in range(2018, 2023):
            for count in range(0, 6):
                try:
                    tables = pd.read_html(f"{url}office={office}&sgkey={count+1}/{key}&Submit=Search", header=0, flavor='html5lib')
                    df1 = tables[0]

                    #merge all DataFrames into one
                    final_df = pd.concat([df1], axis=1)

                    #Display dataframe table on screen
                    print(final_df)

                # Write the dataframe to excel file
                except Exception as e:
                    print(f"Error occurred while processing office {office}, key {key}, count {count+1}: {e}")
                    # do some error handling, e.g. log the error or skip to the next record
                    pass



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


    
    # Variables initialization
    url = 'http://csg.drdlr.gov.za/esio/listdocumentfromkey.jsp?'
    
    # Store the data from table in a variable
    office_codes = []
    office_codes.append(Conn.SGOfficeCodeResult(connect))


    # Loop for currentitem in OfficeCodes
    for currentitem in office_codes:
            
            missingUrl = url+'office='+ '1' +'&sgkey='+ '1' +'&Submit=Search'

            # Run Exception Handler if you get Java.sql.SQLException
            try: 
                missingUrl == 'java.sql.SQLException'
            except jpype.JException(jpype.java.sql.SQLException):
                Conn.OfficeOfflineLog(connect)

            # Run Exception Handler if you get Error
            try:
                response = requests.get(missingUrl)
                missingUrl == 'Error'
            except Exception as e:
                # Handle the exception here
                print("An error occurred while trying to connect to the website:", e)
                Conn.OfficeOfflineLog()


            DataFromWeb = ScapePage(missingUrl)
