import paramiko
import subprocess
import schedule
import os, glob
import time
import shutil

src_dir ="/home/system/Application/jade/data/"
target_dir="/home/ftper/ftp/jade/"

# 1st step is remote query and copy data from jade.
def remote_query_copy():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('10.2.130.18', username='system', password='abc123')
                   
    stdin, stdout, stderr = client.exec_command('python /opt/system/BDA/query.py')

    client.close()
    
    #call transfer function to transfer data to big data server
    transfer()
    return None

# 2st step is secure copy file to 
def transfer():
    files = os.listdir(src_dir)
    for file in files:
        shutil.move(src_dir + file,target_dir) 
    return None

schedule.every().hour.at(":00").do(remote_query_copy)

while True:
    schedule.run_pending()
