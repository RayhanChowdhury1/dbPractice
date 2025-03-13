import sqlalchemy as sa
import sqlalchemy.orm as so

from sm_model.models import User, Post, Comment
import pyinputplus as pyip

class Controller:
    def __init__(self, db_location = 'sqlite:///social_media.db'):
        self.current_user = None
        self.engine = sa.create_engine(db_location)

    def set_current_user(self, name):
        with so.Session(bind=self.engine) as session:
            self.current_user = session.scalars(sa.select(User).where(User.name == name)).one_or_none()

    def get_user_names(self) -> list[str]:
        with so.Session(bind=self.engine) as session:
            user_names = session.scalars(sa.select(User.name).order_by(User.name)).all()
        return list(user_names)

    def get_posts(self, user_name: str) -> list[dict]:
        with so.Session(bind=self.engine) as session:
            user= session.scalars(sa.select(User).where(User.name== user_name)).one_or_none()
            posts_info = [{'title': post.title,
                           'description': post.description,
                           'number_likes': len(post.liked_by_users),
                           }
                          for post in user.posts]
        return posts_info



