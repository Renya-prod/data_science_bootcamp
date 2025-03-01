# filter.jq
. |
[
    "id", "created_at", "name", "has_test", "alternate_url"
], # csv
(
    .items[] | [
        .id,
        .created_at,
        .name,
        .has_test,
        .alternate_url
  ]
) | @csv
