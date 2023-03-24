import pandas as pd
import re
from functools import reduce
import requests
from bs4 import BeautifulSoup



# Write the dataframe to excel file
def WriteToCSV(df1):
    df1.to_csv('SG-Import.csv')
    #df1.to_excel('test_data.xlsx', index=False, header=False)


#Export excel data to csv file
def ExportFromCSV(df1):
     read_file = pd.read_excel (r'test_data.xlsx')
     #read_file.to_csv (r'SG-Import.csv', index = None, header=True)


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
            WriteToCSV(final_df)

