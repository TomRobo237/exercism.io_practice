#!/bin/bash
if test -z "${1}" ; then
	printf 'One for you, one for me.\n'
else
	printf 'One for %s, one for me.\n' "${1}"
fi

