import sqlite3

conn = sqlite3.connect('students.sqlite')
cursor = conn.cursor()

select_students ="""
SELECT id,firstname, lastname
FROM students
WHERE age>=15
"""

group_by_query = """
Select gender,avg(age)
FROM students
GROUP BY gender
"""
average_age_by_gender = cursor.execute(group_by_query).fetchall()

cursor.execute(select_students)
first_student = cursor.fetchone()
more_students= cursor.fetchmany(10)
other_students= cursor.fetchall()
conn.close()

print(other_students)
print(first_student)
print(more_students)
print(average_age_by_gender)