#!/bin/sh

INPUT_FILE="../ex01/hh.csv"

if [ ! -f "$INPUT_FILE" ]; then
    echo "Some error"
    echo "File '$INPUT_FILE' not found."
    exit 1
fi

OUTPUT_FILE="hh_sorted.csv"

head -n 1 "$INPUT_FILE" > "$OUTPUT_FILE"
tail -n +2 "$INPUT_FILE" | sort -t',' -k2,2 -k1,1 >> "$OUTPUT_FILE"

echo "CSV sorted file saved as '$OUTPUT_FILE'."