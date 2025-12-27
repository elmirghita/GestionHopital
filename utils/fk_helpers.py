def get_or_create_id(conn, table, column, value):
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT id_{table} FROM {table} WHERE {column} = %s",
        (value,)
    )
    result = cursor.fetchone()

    if result:
        return result[0]
    else:
        cursor.execute(
            f"INSERT INTO {table} ({column}) VALUES (%s)",
            (value,)
        )
        conn.commit()
        return cursor.lastrowid
