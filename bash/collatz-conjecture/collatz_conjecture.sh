#!/bin/sh

NUM="$1"
STEPS=0

if test "$NUM" -eq "$NUM" && test  "$NUM" -gt 0 ; then
	while test "$NUM" -ne 1 ; do
		if test "$(( NUM % 2 ))" -eq 0 ; then
			NUM="$(( NUM / 2 ))"
			STEPS="$(( STEPS + 1 ))"
		else
			NUM="$(( NUM * 3 + 1 ))"
			STEPS="$(( STEPS + 1))"
		fi
	done
	printf '%s\n' "$STEPS"
else
	printf 'Error: Only positive numbers are allowed\n'
	exit 1
fi
