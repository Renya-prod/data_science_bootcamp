#!/bin/sh

if [ $# -ne 1 ]; then
    echo "Some error"
    echo "Usage file after function, write like this: $0 '../ex00/hh.json'"
    exit 1
fi

INPUT_FILE=$1

if [ ! -f "$INPUT_FILE" ]; then
    echo "Some error"
    echo "File '$INPUT_FILE' not found."
    exit 1
fi

OUTPUT_FILE="hh.csv"

jq -r -f filter.jq "$INPUT_FILE" > "$OUTPUT_FILE"

echo "CSV file saved as '$OUTPUT_FILE'."