#!/bin/bash 

bash script.sh /dev/usb/lp1 >> script.log 2>&1 &
python server.py >> server.log 2>&1 &
