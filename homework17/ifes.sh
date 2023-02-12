!/bin/bash

if (( $1 > 0 ))
then
echo "$1 is positive"
elif [[ $1 -eq 0 ]]
then
echo "$1 is 0"
else
echo "$1 is negative"
fi
