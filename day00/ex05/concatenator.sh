#!/bin/sh

OUTPUT_FILE="hh_combined.csv"

csv_files=$(ls *.csv 2>/dev/null | grep -E "^[0-9]{4}-[0-9]{2}-[0-9]{2}\.csv$")
if [ -z "$csv_files" ]; then
  echo "No partitioned files found."
  exit 1
fi

HEADER=$(head -n 1 $(echo "$csv_files" | head -n 1))
echo "$HEADER" > "$OUTPUT_FILE"

for file in $csv_files; do
  tail -n +2 "$file" >> "$OUTPUT_FILE"
done

echo "CSV files concatenated into '$OUTPUT_FILE'."