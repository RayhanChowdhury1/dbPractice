import sqlite3

conn = sqlite3.connect("sm.sqlite")
cursor = conn.cursor()

q1 = """
SELECT text from comments
WHERE text like '%?'
"""
t =cursor.execute(q1)
for i in t:
    print(i)

q2 = """
UPDATE users set name = 'Lizzy'
WHERE name = 'Elizabeth'
"""
cursor.execute(q2)

q3 = """
SELECT users.name, count(posts.id)
FROM users INNER JOIN posts on posts.user_id = users.id
GROUP BY posts.id
"""
# x = cursor.execute(q3)
# for i in x:
#     print(i)

q4 = """
SELECT users.name, comments.text
FRom users inner join comments on users.id = comments.user_id
GROUP BY users.name
"""
y = cursor.execute(q4)
for i in y:
    print(i)