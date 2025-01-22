import sqlite3

parameterised_insert_query = """
INSERT INTO
users (name, age, gender, nationality)
VALUES
(?,?,?,?);
"""

with sqlite3.connect('sm.sqlite') as conn:
    cursor = conn.cursor()
    cursor.execute(parameterised_insert_query,('James',25,'male','USA'))
    cursor.execute(parameterised_insert_query, ('Leila', 32, 'female', 'France'))
    cursor.execute(parameterised_insert_query, ('Brigitte', 35, 'female', 'England'))
    cursor.execute(parameterised_insert_query, ('Mike', 40, 'male', 'Denmark'))
    cursor.execute(parameterised_insert_query, ('Elizabeth', 21, 'female', 'Canada'))

conn.commit()