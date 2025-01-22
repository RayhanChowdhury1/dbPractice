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

    posts_insert_query = """
        INSERT INTO posts (title,description ,user_id)
         VALUES 
                ('Happy','I am feeling very happy today',1),
                ('Hot weather','The weather is very hot today',2),
                ('Help','I need some help with my work',2),
                ('Great news','I am getting married',1),
                ('Interesting Game','It was a fantastic game of tennis',5),
                ('Party','Anyone up for a late-night party today',3);
          """
    cursor.execute(posts_insert_query)


    comments_insert_query = """
        INSERT INTO comments (text,user_id,post_id)
         VALUES 
                ('Count me in',6,1),
                ('What sort of help?',5,3),
                ('Congrats Buddy',2,4),
                ('I was rooting for Nadal though',4,5),
                ('Help with your thesis?',2,3),
                ('Many Congratulations',5,4);
          """
    cursor.execute(comments_insert_query)

    likes_insert_query = """
        INSERT INTO likes (user_id,post_id)
         VALUES 
                (1,6),
                (2,3),
                (1,5),
                (5,4),
                (2,4),
                (4,2),
                (3,6);
          """
    cursor.execute(likes_insert_query)
conn.commit()