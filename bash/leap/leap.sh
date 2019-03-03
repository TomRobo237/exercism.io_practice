#!/bin/bash
usage(){
printf 'Usage: leap.sh <year>\n'
exit 1
}

year_calc(){
YEAR="$1"
if test "$(( YEAR % 400 ))" -eq 0 ; then
	printf 'true\n'
elif test "$(( YEAR % 100 ))" -eq 0 ; then
	printf 'false\n'
elif test "$(( YEAR % 4 ))" -eq 0 ; then
	printf 'true\n'
else
	printf 'false\n'
fi
}

if test "$#" -gt 1 -o "$#" -eq 0 ; then
	usage
elif ! test "$1" -eq "$1" 2>/dev/null ; then
	usage
else
	year_calc "$1"
fi
