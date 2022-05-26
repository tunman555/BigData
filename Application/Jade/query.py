#!/usr/bin/env python
import datetime
import sys
import time
import psycopg2
import csv 
import datetime
import os 
import json
import subprocess 


f = open('/opt/system/BDA/table_columns.json')
table_columns = json.load(f)
fmt =  "%Y-%m-%d_%H-%M-%S"

def remote_copy(dir):
    p = subprocess.Popen(['scp',"-r",dir , 'system@10.2.130.201:/home/system/Application/jade/data/'])
    sts = os.waitpid(p.pid, 0)    
    print("remote copied")
    return None

def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size
"""
def round_seconds(obj):
    if obj.microsecond >= 500_000:
        obj += datetime.timedelta(seconds=1)
    return obj.replace(microsecond=0.strftime(fmt))
"""
def round_seconds(dateTimeObject):
    newDateTime = dateTimeObject + datetime.timedelta(seconds=.5)
    return newDateTime.replace(microsecond=0)

t = datetime.timedelta(minutes=60)
now = round_seconds(datetime.datetime.now())

start_time = str(now - t) 
end_time = str(now)

try : 
    con = psycopg2.connect(user="jade",
                            password = "jade",
                            host = "127.0.0.1",
                            database = "jade_statistical",
			    port="5433")
    folder_name = now.strftime("%Y-%m-%d_%H-%M-%S")
    os.makedirs("/opt/system/BDA/data/" + folder_name)
    print(start_time,end_time)
    for k in table_columns:
        cur = con.cursor()
        #postgres_cmd=f"select * from {k} where {table_columns[k]} between '{start_time}' and '{end_time}'"
        postgres_cmd="select * from %s where %s between '%s' and '%s'" % (k,table_columns[k],start_time,end_time)
        #postgres_cmd=f"select * from {k} where {table_columns[k]} between '2021-08-01' and '2021-10-02'"
        cur.execute(postgres_cmd)
        record = cur.fetchall()
        #filepath = path.relpath('./jadeQueried/' + str(k+"_") + end_time)

        
        with open ("/opt/system/BDA/data/" + folder_name + "/" +str(k),'w+') as f:
                csvw =csv.writer(f)
                csvw.writerows(record)
    size = get_size(folder_name)
    with open("/opt/system/BDA/jade2BDLog.txt", "w") as text_file :
        if size == 0 : 
            text_file.write("%s  Warning !! File is missing." %(end_time))
            sys.exit()
        else:
            text_file.write("%s  Jade tables was queried and save to file\n" %(end_time))
            text_file.write("%s  File size is %s bytes" %(end_time,size))
        
except (Exception,psycopg2.Error) as error :
    print("Error",error)
finally : 
    if (con):
        cur.close()
        con.close()
        print("Pgadmin3 was closed")
        remote_copy('/opt/system/BDA/data/'+folder_name)

