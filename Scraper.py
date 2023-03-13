import pandas as pd
import re
from functools import reduce



#function to insert integer into string
def data_tables(df1, df2, df3):
    #create DataFrames
    df1 = pd.DataFrame({'team': ['A', 'B', 'C', 'D'],
                        'points': [18, 22, 19, 14]})

    df2 = pd.DataFrame({'team': ['A', 'B', 'C'],
                        'assists': [4, 9, 14]})

    df3 = pd.DataFrame({'team': ['C', 'D', 'E', 'F'],
                        'rebounds': [10, 17, 11, 10]})

    #view DataFrames
    print(df1, '\n')
    print(df2, '\n')
    print(df3, '\n')


def merge_data():
    #create DataFrames
    df1 = pd.DataFrame({'team': ['A', 'B', 'C', 'D'],
                        'points': [18, 22, 19, 14]})

    df2 = pd.DataFrame({'team': ['E', 'F', 'G', 'H'],
                        'points': [4, 9, 14, 10]})

    df3 = pd.DataFrame({'team': ['I', 'J', 'K', 'L'],
                        'points': [10, 17, 11, 10]})

    #define list of DataFrames
    dfs = [df1, df2, df3]

    #merge all DataFrames into one
    final_df = df1.append(df2).append(df3).sort_values('team')

    #view merged DataFrame
    print(final_df)


#Main function
if __name__ == '__main__':
    
    # Variables initialization
    url = 'http://csg.drdlr.gov.za/esio/listdocumentfromkey.jsp?'
    office = 1
    key = 2022


    if office > 0 and office <=5:
        #if key > 2016 and key <= 2020:
            for count in range(0, 5):
                    tables = pd.read_html(f"{url}office={office}&sgkey={count+1}/{key}&Submit=Search", header=0, flavor='bs4')
                    df1 = tables[0]

                    #merge all DataFrames into one
                    final_df = pd.concat([df1], axis=1)

                    #Display dataframe table on screen
                    #print('Tables found:', len(tables))
                    print(final_df)

                    office += 1
                    #key += 1

            # Write the dataframe to excel file
            #df1.to_csv('SG-Import.csv')
            #df1.to_excel('test_data.xlsx', index=False, header=False)

            #Export excel data to csv file
            #read_file = pd.read_excel (r'test_data.xlsx')
            #read_file.to_csv (r'SG-Import.csv', index = None, header=True)




