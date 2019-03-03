#!/bin/sh
INPUT="$1"

if test "$(expr $INPUT : '[0-9]*$')" -eq 0 ; then
# if [[ "$INPUT" =~ [^[:digit:]] ]]; then 
	printf 'Must give positive number!\n' 
	exit 1
fi

LEN="${#INPUT}"
NUM_LIST="$( printf '%s' "$INPUT" | fold -b1 )"
TOTAL='0'
for i in $NUM_LIST ; do
	TOTAL=$(( TOTAL + $(( i ** LEN )) ))
done

test "$INPUT" -eq "$TOTAL" && printf 'true\n' || printf 'false\n'
