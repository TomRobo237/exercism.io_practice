#!/bin/bash

print_greeting(){
	printf 'Hello, %s\n' "$1"
}

if test "$#" -gt 1 ; then
	printf 'Too Many Args.\n'
	exit 1
elif test "$#" -eq 0 ; then
	printf 'Usage: ./error_handling <greetee>'
	exit 1
else 
	print_greeting "$@"
fi
