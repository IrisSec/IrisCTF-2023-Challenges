#!/bin/bash
echo -n "Give me your command: "
read -e -r input
input="exec:./chal ls $input"

# i have to give you stderr
FLAG="irisctf{they_even_fixed_it_for_unbalanced_double_quotes}" socat - "$input" 2>&0
