import glob
import schedule
import time
import os
import shutil 

def get_latest(path):
        list_of_files = glob.glob(path + '/*.gz')
        if len(list_of_files) != 0:
                return max(list_of_files,key = os.path.getctime)
        else :
                return None
cat = ['RADAR','ADSB','CAT62']

wd = "/home/system/asterix_collection/"
target_dir = '/home/ftper/data/'

def job():
        for i in cat:
                site_addr = glob.glob(wd + "data/" + i + "/*")
                for j in site_addr:
                        latest_file = get_latest(j)

                        if latest_file != None :
                                src_type = latest_file.split('/')[5]
                                main = latest_file.split('/')[6][-1]
                                if src_type == 'RADAR' and main=='1':
                                        shutil.move(latest_file, target_dir + '/RADAR/' + j)
                                elif src_type == 'ADSB':
                                        shutil.move(latest_file, target_dir + '/ADSB/' + j)
                                elif src_type == 'CAT62':
                                        if latest_file.split('/')[6] =='ACC62':
                                                shutil.move(latest_file, target_dir + '/CAT62/' + j)

                        else : pass

schedule.every().hour.at(":00").do(job)
while True:
        schedule.run_pending()
