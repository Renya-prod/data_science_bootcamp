#!/bin/sh

INPUT_FILE="../ex03/hh_positions.csv"

if [ ! -f "$INPUT_FILE" ]; then
    echo "Some error"
    echo "File '$INPUT_FILE' not found."
    exit 1
fi

HEADER=$(head -n 1 "$INPUT_FILE")

tail -n +2 "$INPUT_FILE" |
while IFS=',' read -r id created_at name has_test alternate_url; do
    date=$(echo "$created_at" | cut -d'T' -f1 | tr -d '"')
    if [ -n "$date" ]; then
        if [ ! -f "${date}.csv" ]; then
            echo "$HEADER" > "${date}.csv"
        fi
        echo "$id,$created_at,$name,$has_test,$alternate_url" >> "${date}.csv"
    fi
done

echo "Data partitioned by dates into separate files."