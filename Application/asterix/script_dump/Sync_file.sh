#!/bin/bash

ssh root@baccsda1alis `rsync -zarv --include "*/" --include="*.gz" --exclude="*" "root@baccsda1alis:/opt/system/rec_RADAR_data_zip/CMA1" "system@10.82.130.156:/home/system/asterix_collection/data/CMA1_RADAR"`
