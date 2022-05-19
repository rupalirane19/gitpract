import pandas
from sqlalchemy import create_engine

path = r'C:\Users\USER\Desktop\studinfo.xlsx'
df = pandas.read_excel( path )
print(df)
con = 'postgresql://postgres:pass123@localhost/datapract'
db = create_engine (con )
con1 = db.connect( )
try:
    df.to_sql ( 'stud1' , con1 , if_exists = 'append' , index = False , schema = 'test' )
    print("data in")
except Exception as e :
    print(e)

