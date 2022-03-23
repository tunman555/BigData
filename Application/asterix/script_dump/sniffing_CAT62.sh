#!/bin/bash

#record all data

#path_rec_RADAR="/opt/system/rec_ALL_data_zip"
path_rec_RADAR="/home/system/asterix_collection/data/CAT62"

#script for ACC62, dport = 43046
	ssh root@10.82.130.156 "tcpdump -nnXs 0 -i enp10s0f1 udp port 38046 and dst 224.8.48.1 -s0 -vvv -G 1800 -w ${path_rec_RADAR}/ACC62/ACC62_%Y%m%d_%H%M%S.pcap -z gzip -Z root > /dev/null 2>&1 &"


#script for ADSB62, dport = 43172

	ssh root@10.82.130.156 "tcpdump -nnXs 0 -i enp10s0f1 udp port 38172 and dst 224.8.48.1 -s0 -vvv -G 1800 -w ${path_rec_RADAR}/ADSB62/ADSB62_%Y%m%d_%H%M%S.pcap -z gzip -Z root > /dev/null 2>&1 &"



#script for RAD62, dport = 43158

        ssh root@10.82.130.156 "tcpdump -nnXs 0 -i enp10s0f1 udp port 38158 and dst 224.8.48.1 -s0 -vvv -G 1800 -w ${path_rec_RADAR}/RAD62/RAD62_%Y%m%d_%H%M%S.pcap -z gzip -Z root > /dev/null 2>&1 &"

