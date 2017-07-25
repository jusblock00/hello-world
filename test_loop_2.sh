#! /bin/bash

# Assign variable y a value of 0
y=0

# Repeat outer loop 3 times
for y in 1 2 3
do

    # Repeat inner loop 3 times
    for x in "Monday" "Tuesday" "Wednesday"
    do

    # Print the variable x
        echo $x
    done

    # Print a blank line
    echo " "
done
