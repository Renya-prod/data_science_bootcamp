#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Some error"
    echo "Usage vacancy after function, write like this: $0 'data scientist'"
    exit 1
fi

VACANCY_NAME=$1
ENCODED_VACANCY_NAME="${VACANCY_NAME// /+}"

URL="https://api.hh.ru/vacancies?text=${ENCODED_VACANCY_NAME}&per_page=20"

curl "$URL" | jq '{
  page: .page,
  found: .found,
  clusters: .clusters,
  arguments: .arguments,
  per_page: .per_page,
  pages: .pages,
  items: .items
}' > hh.json

echo "Saved in 'hh.json'."