#!/bin/bash

temp=$1

if [ $temp -lt 55 ]; then
    echo "freezing"
elif [ $temp -lt 85 ]; then
    # we are nore in the range of 55-85 exclusive
    if [ $temp -lt 67 ]; then
        echo "cold"
    # if greater than 67
    else
        echo "nice"
    fi
# if greater than 85
else
    echo "hot"
fi
