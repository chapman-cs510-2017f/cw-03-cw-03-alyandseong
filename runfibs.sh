#!/bin/bash
 
#fib.py for arguments 1 to 10000
 
if [ -f "fibs.csv.bak" ]
then
    echo "Error- file and back-up file already exist"
    exit 1
fi
 
if [ -f "fibs.csv" ]
then
    mv fibs.csv fibs.csv.bak
    echo "Back-up file created: file fibs.csv.back"
else
    for n in {1..10000}; do
    echo -n "$(./fib.py $n)," >> fibs.csv
    done
fi
