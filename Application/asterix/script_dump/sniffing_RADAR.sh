#!/bin/bash

#varied by time

path_script_dump="/home/system/asterix_collection/script_dump"
path_rec_RADAR="/home/system/asterix_collection/data/RADAR"

for i in `cat ${path_script_dump}/RADAR_IP` ; do
	RADAR_name=`echo ${i}|awk -F, '{print $1}'`
	RADAR_ip=`echo ${i}|awk -F, '{print $2}'`
	echo ${RADAR_name}
	echo ${RADAR_ip}
#	echo ${i}
#	ssh root@baccsda1bli "tcpdump -i eth2 -s0 -vv host ${i} -C 1 -w ${path_rec_RADAR}/${i}/dump_`date +"%Y%m%d"`_`date +"%H%M%S"`.pcap > /dev/null 2>&1 &"
#        ssh root@baccsda1bli "tcpdump -i eth2 -s0 -vv host ${RADAR_ip} -C 1 -w ${path_rec_RADAR}/${RADAR_ip}/${RADAR_name}_`date +"%Y%m%d"`_`date +"%H%M%S"`.pcap > /dev/null 2>&1 &"
	ssh root@10.82.130.156 "tcpdump -i enp10s0f0 -s0 -vvv host ${RADAR_ip} -G 3600 -w ${path_rec_RADAR}/${RADAR_name}/${RADAR_name}_%Y%m%d_%H%M%S.pcap -z gzip -Z root > /dev/null 2>&1 &"

done
