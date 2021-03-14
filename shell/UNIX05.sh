#!/bin/sh
##=======================================================================================##
## script : UNIX05.sh                                                                    ##
## Script Description : To find out list of unique valid dates with format (yyyy-mm-dd)  ##
## Author : Chinmoy                                                                      ##
##=======================================================================================##
echo "The unique valid dates are"
file=$1
extract=$(cat $file | tail -n +2 | cut -d ',' -f3 | uniq)
format="+%Y-%m-%d"
for d in $extract
do
	if [[ "$d" == "$(date "+%Y-%m-%d" -d "$d" 2>/dev/null)" ]];then
		echo $d
	fi
done
exit 0
