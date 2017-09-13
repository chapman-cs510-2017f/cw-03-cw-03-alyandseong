#!/bin/bash

#fib.py for arguments 1 to 10000


if [n > 1 and n <= 10000]; then
	echo fibonacci(int(n))
	
fi

n = n + 1

#output to fibs.csv, if already fibs.csv then move file to fibs.csv.bak and create new fibs.csv
# if backup exists then print error

if [-f fibs.csv.bak]
then
	echo "Error- file and back-up file already exist"

elif [-f fibs.csv]
then
	mv fibs.csv fibs.csv.bak

else
	
fi
	
	 


