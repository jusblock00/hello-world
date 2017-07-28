#!/bin/bash

# This script multiplies two numbers

# Assign variables
X=0 # Number 1
Y=0 # Number 2
Z=0 # Product of Numbers

# For variable X from 1 to 5
for ((X=1; X<=5; X++))
do
    for ((Y=1; Y<=2; Y++))
    do
        for ((W=1; W<=3; W++))
        do
            Z=$(( $X * $Y * $W )) # Calculate product
            #echo "X = $X; Y = $Y; W = $W; X * Y * W = $Z" COMMENTED OUT
            #echo " " COMMENTED OUT
    done

    echo "Y is changing!"
    echo " " # Blank line
done

    echo "X is changing!"
    echo " " # Blank line
    sleep 3 # Pause process when X changes

    if (( $Z > 10 ))
    then
        echo "X = $X; Y = $Y; W = $W; X * Y * W = $Z" # Print variables and product
        echo " " # Blank line
    fi
done

# Print that the script is done
echo "Done!"
