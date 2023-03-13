import time
import bs4
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import csv
import pandas as pd


# Variables initialization
url = 'http://csg.drdlr.gov.za/esio/listdocumentfromkey.jsp?'
office = 1
key = 2017

#Open CSV file
filename = 'SG-Import.csv'
f = open(filename,'w',newline = '')
sg_file = csv.writer(f)

if office > 0 and office <=5:
    for count in range(0, 5):
        # Connect to HTML page and scrape the table tag
        html = urlopen(f"{url}office={office}&sgkey={count+1}/{key}&Submit=Search")
        bsobj = soup(html.read(), features="lxml")
        tbody = bsobj('table', id='Table1')[0].findAll('tr')
        xl = []


    for row in tbody:
        cols = row.findChildren(recursive = False)
        cols = [element.text.strip() for element in cols]
        xl.append(cols)

        df = pd.DataFrame(data=xl, column=(cols))
        df.to_csv('SG-Import.csv', index=False,header=False)
        #http://csg.drdlr.gov.za/esio/listdocumentfromkey.jsp?office=2&sgkey=2/2020&Submit=Search
        print(df)
    #time.sleep(5,5)
