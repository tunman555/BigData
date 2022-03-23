#!/bin/bash

#varied by time

path_script_dump="/home/system/asterix_collection/script_dump"
#path_rec_ADSB="/opt/system/rec_ADSB_data_zip"
path_rec_ADSB="/home/system/asterix_collection/data/ADSB"

for i in `cat ${path_script_dump}/ADSB_IP` ; do
	ADSB_name=`echo ${i}|awk -F, '{print $1}'`
	ADSB_ip=`echo ${i}|awk -F, '{print $2}'`
	echo ${ADSB_name}
	echo ${ADSB_ip}
#	echo ${i}
#	ssh root@baccsda2ali "tcpdump -i eth2 -s0 -vv host ${i} -C 1 -w ${path_rec_ADSB}/${i}/dump_`date +"%Y%m%d"`_`date +"%H%M%S"`.pcap > /dev/null 2>&1 &"
#        ssh root@baccsda2ali "tcpdump -i eth2 -s0 -vv host ${ADSB_ip} -C 1 -w ${path_rec_ADSB}/${ADSB_ip}/${ADSB_name}_`date +"%Y%m%d"`_`date +"%H%M%S"`.pcap > /dev/null 2>&1 &"
	ssh root@10.82.130.156 "tcpdump -i enp10s0f0 -s0 -vvv host ${ADSB_ip} -G 3600 -w ${path_rec_ADSB}/${ADSB_name}/${ADSB_name}_%Y%m%d_%H%M%S.pcap -z gzip -Z root > /dev/null 2>&1 &"

done


