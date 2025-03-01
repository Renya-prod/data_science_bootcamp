#!/bin/sh

INPUT_FILE="../ex02/hh_sorted.csv"

if [ ! -f "$INPUT_FILE" ]; then
    echo "Some error"
    echo "File '$INPUT_FILE' not found."
    exit 1
fi

OUTPUT_FILE="hh_positions.csv"

head -n 1 "$INPUT_FILE" > "$OUTPUT_FILE"
tail -n +2 "$INPUT_FILE" | awk -F ',' '
BEGIN {
    OFS = ",";
}
{
    id = $1
    created_at = $2
    name = $3
    has_test = $4
    alternate_url = $5

    cleaned_name = ""
    if (name ~ /Junior/) {
        cleaned_name = cleaned_name "Junior"
    }
    if (name ~ /Middle/) {
        cleaned_name = (cleaned_name == "" ? "" : cleaned_name "/") "Middle"
    }
    if (name ~ /Senior/) {
        cleaned_name = (cleaned_name == "" ? "" : cleaned_name "/") "Senior"
    }
    if (cleaned_name == "") {
        cleaned_name = "-"
    }
    
    print id, created_at, "\"" cleaned_name "\"", has_test, alternate_url
}
' >> "$OUTPUT_FILE"

echo "CSV cleaned file saved as '$OUTPUT_FILE'."