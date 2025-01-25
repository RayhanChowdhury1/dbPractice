import sqlite3
from tabulate import tabulate

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")
    return result

# select_users = "SELECT * from users"

with sqlite3.connect("sm.sqlite") as conn:

#     users = execute_read_query(conn, select_users)
#
# for user in users:
#     print(user)

    # select_users_post = """
    # SELECT users.id, users.name, posts.description
    # FROM posts
    # INNER JOIN users ON users.id = posts.user_id
    # """
    #
    # users_posts = execute_read_query(conn, select_users_post)
    # for users_post in users_posts:
    #     print(users_post)

    # select_post_comments_users= """
    # SELECT posts.description as post, comments.text as comment, name
    # FROM posts
    # JOIN comments ON posts.id = comments.post_id
    # JOIN users ON users.id = comments.user_id
    # """
    #
    # posts_comments_user = execute_read_query(conn, select_post_comments_users)
    #
    # for posts_comments_user in posts_comments_user:
    #     print(posts_comments_user)
