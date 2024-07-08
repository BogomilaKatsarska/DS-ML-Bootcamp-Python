import pandas as pd
import numpy as np

'''
libraries:
- sqlalchemy
- lxml
- html5lib
- BeautifulSoup4

- xlrd
'''
from sqlalchemy import create_engine
df = pd.read_csv('username.csv')
print(df)
df.to_csv('my_output', index=False)
# pd.read_excel('excel_sample.xlsx', sheetname='Sheet1')
# df.to_excel('excel_sample2.xlsx', sheet_name='new_sheet')
data = pd.read_html('https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/')
print(data[0])

engine = create_engine('sqlite:///:memory:')
# df.to_sql('my_table', engine)
# sqldf = pd.read_sql('my_table', con=engine)
# print(sqldf)