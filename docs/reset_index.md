# Delete Data and Reset Index

Connect to DB using Beekeeper Studio

Delete by id: 

```sql
DELETE FROM your_table_name WHERE id BETWEEN 6182 AND 6368;
```

Includes 6182 and 6368 (last)



Then, reset index:

```sql
SELECT setval('graphql_api_playerdatatotalsplayoffs_id_seq', COALESCE((SELECT MAX(id) FROM graphql_api_playerdatatotalsplayoffs), 1), false);
```

Return value should be last id seq. Next insert will start after.

---

Given the table name `graphql_api_playerdatatotalsplayoffs`, the corresponding sequence name for the primary key (`id`) in a PostgreSQL database managed by Django would likely follow the format `<table_name>_id_seq`. This is the default naming convention Django uses for primary key sequences in PostgreSQL.

To reset the sequence for the `id` primary key after deleting certain records (or if you want to ensure the sequence is correct), you would use the `setval` function with the correct sequence name. Based on your table name, the SQL command would look something like this:

```sql
SELECT setval('graphql_api_playerdatatotalsplayoffs_id_seq', COALESCE((SELECT MAX(id) FROM graphql_api_playerdatatotalsplayoffs), 1), false);
```

This command performs the following actions:

1. `SELECT MAX(id) FROM graphql_api_playerdatatotalsplayoffs`: Finds the highest `id` currently in the `graphql_api_playerdatatotalsplayoffs` table.
2. `COALESCE(..., 1)`: If the table is empty (meaning the `SELECT MAX(id)` returns `null`), it defaults to `1` to ensure the sequence starts at the beginning.
3. `setval('graphql_api_playerdatatotalsplayoffs_id_seq', ..., false)`: Sets the sequence for the `id` column in the `graphql_api_playerdatatotalsplayoffs` table to the value obtained from the `COALESCE` function. The `false` parameter ensures that the next value used for the `id` will be the next integer after the maximum `id` found in the table, maintaining the integrity and continuity of your primary keys.

This command is useful for maintaining sequential integrity, especially after manual deletions or adjustments in the table, ensuring that new records are inserted with the correct `id`.