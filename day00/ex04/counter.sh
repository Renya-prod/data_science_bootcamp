#!/bin/sh

INPUT_FILE="../ex03/hh_positions.csv"

if [ ! -f "$INPUT_FILE" ]; then
    echo "Some error"
    echo "File '$INPUT_FILE' not found."
    exit 1
fi

OUTPUT_FILE="hh_uniq_positions.csv"

{
    echo "\"name\",\"count\""
    tail -n +2 "$INPUT_FILE" |
    awk -F ',' '{print $3}' |
    tr -d '"' |
    sort |
    uniq -c |
    sort -r -n |
    awk '{print "\"" $2 "\"," $1}'
} > "$OUTPUT_FILE"

echo "CSV file saved as '$OUTPUT_FILE'."