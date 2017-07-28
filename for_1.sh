#!/bin/bash

# For variable count form 1 to 100
for ((count=1; count<=100; count++))
do
	echo $count
    mkdir "tabby_$count"
    touch "file_$count"
    mv "file_$count" "tabby_$count"
    rm -r "tabby_$count"
done
