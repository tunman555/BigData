#!/bin/bash

#record all data

#path_rec_RADAR="/opt/system/rec_ALL_data_zip"
path_rec_RADAR="/home/system/asterix_collection/data/CAT62"

	ssh root@10.82.130.156 "tcpdump -i enp10s0f1 host 224.8.48.1 -s0 -vvv -G 1800 -w ${path_rec_RADAR}/cat62_%Y%m%d_%H%M%S.pcap -z gzip -Z root > /dev/null 2>&1 &"



