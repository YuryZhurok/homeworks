#1/bin/bash

echo "Enter 1 symbol:"
read a
case $a in [[:lower:]])
echo "Letter in the low register";;
[[:upper:]])
echo "Letter in the high register";;
[0-9])
echo "It's a number";;
*)
echo "It's a special symbol";;
esac
