#!/bin/bash

echo "Enter number:"
read a
if (( $a<-1 )) || [[ $a -eq 45 ]]
then
echo "$a is right number"
else
echo "$a isn't right number"
fi
