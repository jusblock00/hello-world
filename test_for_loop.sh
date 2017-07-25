#! /bin/bash
y=0

for ((x=1; x<11; x++))
do
    for ((y=1;y<11; y++))
    do
        ((y=$y+$x))
        echo $y
    done
done
