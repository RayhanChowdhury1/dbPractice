import sqlite3

conn = sqlite3.connect('students.sqlite')
cursor = conn.cursor()

clear_students_table = """
DELETE from students
"""

cursor.execute(clear_students_table)
conn.commit()