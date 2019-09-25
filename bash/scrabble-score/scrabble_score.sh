#!/bin/sh

SCORE=0
LETTERS="$( printf '%s' "$1" |
	awk '{ split( tolower($0) , word , "") 
	for ( i=1 ; i<=length($0); i++ ) { 
		printf( "%s " , word[i] )} }
	')"

for i in $LETTERS ; do
	case "$i" in
		[aeioulnrst]) SCORE="$(( SCORE + 1 ))" ;;
		[dg])         SCORE="$(( SCORE + 2 ))" ;;
		[bcmp])       SCORE="$(( SCORE + 3 ))" ;;
		[fhvwy])      SCORE="$(( SCORE + 4 ))" ;;
		k)            SCORE="$(( SCORE + 5 ))" ;;
		[jx])         SCORE="$(( SCORE + 8 ))" ;;
		[qz])        SCORE="$(( SCORE + 10 ))" ;;
	esac
done

printf '%s\n' "${SCORE}"
