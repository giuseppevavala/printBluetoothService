#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo `date`: "Illegal number of parameters"
else
	while true
	do
	        for f in *.txt
        	do
			if [ $f != "*.txt" ]
			then
                		echo `date`: "Stampando file $f"
	                	echo -e `cat $f` > $1
	        	        rm -fr $f
			fi
	        done
        	sleep 1s
	done
fi

