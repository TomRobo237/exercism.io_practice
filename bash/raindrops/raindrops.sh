#!/bin/bash

factor_and_echo(){
n="$1"
# Wanted to use brace expansion instead of seq as its not a builtin
for i in $(eval printf '%s\ ' {1..$n}) ; do
# test against modulus probs more efficent. But I kinda like this
	if test "$(( n / i * i ))" -eq "$n" ; then
		if test "$i" -eq 3 ; then
			printf 'Pling'
			FACTORED="YES"	
		elif test "$i" -eq 5 ; then
			printf 'Plang'
			FACTORED="YES"	
		elif test "$i" -eq 7 ; then
			printf 'Plong'
			FACTORED="YES"	
		fi
	fi
done

if test -z "${FACTORED}" ; then
	printf '%s\n' "$n"
else
	printf '\n'
fi
}

# Not testing for it but doesn't hurt
if test "$#" -eq 1 -a "$1" -eq "$1" 2>/dev/null ; then
	factor_and_echo "$1"
else
	printf 'Not A Number or no number!\n'
fi
