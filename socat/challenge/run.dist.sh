#!/bin/bash
echo -n "Give me your command: "
read -e -r input
input="exec:./chal ls $input"

# i have to give you stderr
FLAG="fakeflg{REDACTED}" socat - "$input" 2>&0
