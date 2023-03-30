import pandas as pd
import re
import jpype
from functools import reduce
import requests
from bs4 import BeautifulSoup
from Connection import connect
from Execute import SGOfficeCodeResult, MissingDocuments, Display_SGDocument
from Insert import OfficeOfflineLog, SGDocumentPages, SGDocument



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
    
    # Variables initialization
    url = 'http://csg.drdlr.gov.za/esio/listdocumentfromkey.jsp?'


    office_codes = SGOfficeCodeResult()

    # Loop for currentitem in OfficeCodes
    for currentitem in office_codes:
        # Get all the records from vw_MissingDocuments View
        MissingDocuments()

        # Loop for currentitem in OfficeCodes
        for missingDoc in office_codes:
            missingUrl = url+'office='+missingDoc[sgOfficeCode]+'&sgkey='+missingDoc[DocNr]+'&Submit=Search'
            # Run Exception Handler if you get Java.sql.SQLException
            if missingDoc == 'java.sql.SQLException':
                try: 
                    OfficeOfflineLog()
                except jpype.JException(jpype.java.sql.SQLException):
                    pass

            # Run Exception Handler if you get Error
            if missingDoc == 'Error':
                try:
                    response = requests.get(url)
                    OfficeOfflineLog()
                except Exception as e:
                    pass

            DataFromWeb = ScapePage(url)

            # Write to FORM_SGDocuments if Data for Web is > 1
            if DataFromWeb.RowsCount > 1:
                SGDocument()

                DOC_ID = SGDocument()

                FailedCount = 0

                # loop currentitem in Webpage
                for currentitem in DataFromWeb:
                    # if currentitem [0] = 'DOCUMENT NO': (Do nothing)
                    if currentitem [0]:
                        break
                    else:
                        # else Split text, 
                        TextList = currentitem.split()

                        # AND Write to FORM_SGDocumentPage
                        SGDocumentPages()

            FailedCount = FailedCount + 1

    ProcessingYear = 2023


    for currentitem2 in office_codes:
        
        FailedCount = 0

        SGOfficeCode = currentitem2[0]

        StartIndex = 10000000

        if 'file exists':
            print('read text')
            LoopIndex = StartIndex - 30
        else:
            print('')

        LoopIndex = 0

    while FailedCount < 45:
        LoopIndex = LoopIndex + 1
        DocNumber = LoopIndex / ProcessingYear
        QueryResult = Display_SGDocument()

        # if QueryResult [0][0] = 0:
        if QueryResult [0][0]:
            # Wait 3 second

            # Go to web page

            # Run Exception Handler if you get Java.sql.SQLException
            if DocNumber == 'java.sql.SQLException':
                try: 
                    OfficeOfflineLog()
                except Exception as e:
                    pass

            # Run Exception Handler if you get Error
            if DocNumber == 'Error':
                try: 
                    OfficeOfflineLog()
                except Exception as e:
                    pass

            DataFromWeb = ScapePage(url)

            # Write to FORM_SGDocuments if Data for Web is > 1
            if DataFromWeb.RowsCount > 1:
                SGDocument()

                DOC_ID = SGDocument()

                FailedCount = 0

                # loop currentitem in Webpage
                for currentitem in DataFromWeb:
                    # if currentitem [0] = 'DOCUMENT NO': (Do nothing)
                    if currentitem [0]:
                        break
                    else:
                        # else Split text, 
                        TextList = currentitem.split()

                        # AND Write to FORM_SGDocumentPage
                        SGDocumentPages()
            else:
                FailedCount = FailedCount + 1
        
        # Write text to file

    connect.close()
     