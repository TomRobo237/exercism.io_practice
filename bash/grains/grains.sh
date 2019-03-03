#!/bin/bash
# This problem is just 2^0-indexed square...
if test "$1" == "total" ; then
	printf '2^64-1\n' | bc
elif test "$1" -gt 0 -a "$1" -lt 65 ; then 
	printf '2^%s\n' "$(( $1 - 1 ))" | bc
else
	printf 'Error: invalid input\n'
	exit 1
fi
