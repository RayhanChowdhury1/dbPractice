import sqlite3
from faker import Faker
import random
fake=Faker('en_GB')

parameterised_insert_query ="""

INSERT INTO
students (firstname, lastname, age, gender)
VALUES
(?,?,?,?);


"""

conn = sqlite3.connect('students.sqlite')

with sqlite3.connect('students.sqlite') as conn:
    cursor = conn.cursor()
    insert_query = """
    INSERT INTO students (firstname,lastname ,age,gender)
     VALUES 
            ('Milan','Gal',69,'Eye of Rah'),
            ('Eleanore','Shiner',1000,'amogus'),
            ('Rayhan','Chowdhury','Eternal','Existence'),
            ('Denys','Zazuliak',0,'GOD'),
            ('Adam','Reeves',16,'Male'),
            ('Sami','Hafezgi',100,'Soliaire');
            
    """

    fake.random.seed(4321)
    random.seed(4321)
    for _ in range(10):
        f_name = fake.first_name()
        l_name = fake.last_name()
        age = random.randint(11,18)
        gender = random.choice(('Male','Female'))
        cursor.execute(parameterised_insert_query,(f_name,l_name,age,gender))


    cursor.execute(insert_query)

    conn.commit()

