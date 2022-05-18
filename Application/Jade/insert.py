import datetime
import sys
import time
import psycopg2
import csv 
import datetime
import os 
import json
import pathlib

path = sys.argv[1]
#path = str(max(pathlib.Path("C:\\Users\\Public\\").glob('*/'), key=os.path.getmtime)).replace('WindowsPath(','').replace('(','').replace(')','')

# create column name of each table 
def str_tmp_col(list_col): 
    txt =""
    for i in list_col :
         txt = txt + i +" text" + ","
    return txt[:len(txt)-1]

# create column and cast datatype
def cast_text_(table):
    txt = "" 
    for col,dtype in zip(all_coln_dtype[table][0],all_coln_dtype[table][1]):
        txt = txt + f"NULLIF({col},'')::{dtype} ,"
    txt = txt[:len(txt)-1]
    return txt

f = open('./all_coln_dtype.json')
all_coln_dtype = json.load(f)

con = psycopg2.connect(user="jade",
                        password = "jade",
                        host = "127.0.0.1",
                        database = "jade-statistical")
cur = con.cursor()

for table in all_coln_dtype:
    file = path + '/' + table
    tmp_col,tmp_dtype =  all_coln_dtype[table][0],all_coln_dtype[table][1]
    tmp_col_str = ",".join(tmp_col)
    #tmp_dtype_str = ",".join(tmp_dtype)
    col_name = str_tmp_col(tmp_col) #col name + text is used in tmp_table
    cast_text = cast_text_(table) #cast after select from tmp_table
    
    cur.execute(f"""CREATE TEMP TABLE tmp_table ({col_name}) ON COMMIT DROP ;
    
                
                --COPY tmp_table({tmp_col_str}) FROM {file} CSV DELIMITER ',';
                COPY tmp_table({tmp_col_str}) FROM '{file}' CSV HEADER DELIMITER ',' QUOTE '"';
                
                INSERT INTO {table}
                    select {cast_text}
                FROM tmp_table ON CONFLICT DO NOTHING;
                """)
    
cur.close()
con.close()