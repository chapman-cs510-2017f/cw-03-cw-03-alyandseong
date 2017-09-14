#!/bin/bash

#fib.py for arguments 1 to 10000

if [-f fibs.csv.bak]
then
    echo "Error- file and back-up file already exist"
    exit 1

elif [-f fibs.csv]
then
    mv fibs.csv fibs.csv.bak

else
    for n in {1..10000}; do

    ./fib.py $n >> fibs.csv

    done

# for the csv file:

# remove new lines in csv file and switch to commas
# echo a delete character
echo -n ''#special code to delete ,'' # creates comma

