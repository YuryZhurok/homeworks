#!/bin/bash

PS3='Do you want to download python?:'
echo
select a in "Yes" "No"
do
if [[ $a == "Yes" ]]
then
echo "You chose downloading python" && break
else
echo "Get out of there and close the door" && break
fi
done