#!/bin/bash

# in class example
# set age input
#ageinput=$1
#if [ $ageinput -lt 13 ]; then
#    echo "You are a child"
#else
#    echo "Teen here"
#fi

ageInput=$1

if [ $ageInput -lt 13 ]; then 
    echo "child"
elif [ $ageInput -lt 20 ]; then
    echo "teen"
elif [ $ageInput -lt 65 ]; then
    echo "adult"
elif [ $ageInput -gt 65 ]; then
    echo "elderly"
fi
