#!/bin/sh
# shell script to prepend i3status with more stuff

i3status | while :
do
	read line
	a=$(php /home/victor/Documents/Fortnox/Git/phptid/tid_earliest.php)
	#b=$(sudo i3status)
	echo "$line | $a" || exit 1
done
