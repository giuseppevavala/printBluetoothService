#!/bin/bash

while true
do
	for f in *.txt
	do
  		echo "Stampando file $f"
  		echo -e `cat $f` > /dev/usb/lp1
		rm -fr $f
	done
	sleep 1s
done
