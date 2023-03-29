import pandas as pd
import re
from functools import reduce
import requests
from bs4 import BeautifulSoup



#Main function
if __name__ == '__main__':
    
    # Variables initialization
    url = 'http://csg.drdlr.gov.za/esio/listdocumentfromkey.jsp?'
    page = requests.get(url, timeout=10)
    office = 1
    key = 2023
    page_number = 1


    for office in range(1, 11):
        for key in range(2018, 2023):
            for count in range(0, 6):
                try:
                    tables = pd.read_html(f"{url}office={office}&sgkey={count+1}/{key}&Submit=Search", header=0, flavor='html5lib')
                    df1 = tables[0]

                    #merge all DataFrames into one
                    final_df = pd.concat([df1], axis=1)

                    #Display dataframe table on screen
                    #print('Tables found:', len(tables))
                    print(final_df)

                    #page_content = page.content
                    #print(page_content)

                    #soup = BeautifulSoup(page.content, 'html.parser')
                    #print(soup.prettify())


                # Write the dataframe to excel file
                except Exception as e:
                    print(f"Error occurred while processing office {office}, key {key}, count {count+1}: {e}")
                    # do some error handling, e.g. log the error or skip to the next record
                    pass







# Run Exception Handler if you get Java.sql.SQLException

# Run Exception Handler if you get Error

# Write to FORM_SGDocuments if Data for Web is > 1
    # loop currentitem in Webpage
        # if currentitem [0] = Doc No. (Do nothing)
        # else (Split text), (Write to FORM_SGDocumentPage)


