#!/bin/sh

sum_of_square() {
	countdown="$1"
	total=0
	while test "$countdown" -gt 0 ; do
		total=$(( total + countdown * countdown ))
		countdown=$(( countdown - 1 ))
	done
	printf '%s\n' "$total"
}

square_of_sum() {
	countdown="$1"
	total=0
	while test "$countdown" -gt 0 ; do
		total=$(( total + countdown ))
		countdown=$(( countdown -1 ))
	done
	total=$(( total * total ))
	printf '%s\n' "$total"
}

diff_of_squares() {
	squ="$( square_of_sum "$1" )"
	sum="$( sum_of_square "$1" )"
	printf '%s\n' "$(( squ - sum ))"
}

case $1 in
	'sum_of_squares') sum_of_square   "$2" ;;
	'square_of_sum' ) square_of_sum   "$2" ;;
	'difference'    ) diff_of_squares "$2" ;;
esac

