import glob
import schedule
import time
import os 
import subprocess

def get_latest(path):
	list_of_files = glob.glob(path + '/*.gz')
	if len(list_of_files) != 0:
		return max(list_of_files,key = os.path.getctime)
	else :
		return None
cat = ['RADAR','ADSB','CAT62']

def job():
	for i in cat:
		site_addr = glob.glob("../data/" + i + "/*")
		for j in site_addr:
			print(j)
		
			latest_file = get_latest(j)
			if latest_file != None :
		
				src_type = latest_file.split('/')[2].split('\\')[0]
		
				if src_type == 'RADAR':
					subprocess.call("python ./asterix_decode_cat48.py " + latest_file,shell=True)
		
				elif src_type == 'ADSB':
                        		subprocess.call("python ./asterix_decode_cat21.py " + latest_file,shell=True)
				elif src_type == 'CAT62':
					if latest_file.split('/')[3] =='ACC62':
                        			subprocess.call("python ./asterix_decode_ACC62.py " + latest_file,shell=True)
					elif latest_file.split('/')[3] =='ADSB62':
                                                subprocess.call("python ./asterix_decode_ADSB62.py " + latest_file,shell=True)
					elif latest_file.split('/')[3] =='RAD62':
                                                subprocess.call("python ./asterix_decode_RAD62.py " + latest_file,shell=True)

			else : pass

schedule.every().hour.at(":04").do(job)

while True:
	schedule.run_pending()
	time.sleep(1)
