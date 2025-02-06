from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so

class Base(so.DeclarativeBase):
    pass

likes = sa.Table("likes",
                             Base.metadata,
                             sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
                             sa.Column("user_id", sa.ForeignKey("users.id", )),
                             sa.Column("post_id", sa.ForeignKey("posts.id"), ),
                             sa.UniqueConstraint("user_id", "post_id")
                             )

class User(Base):
    __tablename__ = "users"
    id: so.Mapped[int] = so.mapped_column(primary_key=True, autoincrement=True)
    name: so.Mapped[str] = so.mapped_column(unique=True)
    age: so.Mapped[int] = so.mapped_column()
    gender: so.Mapped[str] = so.mapped_column()
    nationality: so.Mapped[str] = so.mapped_column()


    def __repr__(self) -> str:
        return f"User {self.name}"

class Post(Base):
    __tablename__ = 'posts'
    id: so.Mapped[int] = so.mapped_column(primary_key=True, autoincrement=True)
    title: so.Mapped[str] = so.mapped_column()
    description: so.Mapped[str] = so.mapped_column()
    user: so.Mapped[list["User"]] = so.relationship('User',back_populates='posts')
    user_id: so.Mapped[list[User]]= so.mapped_column(sa.ForeignKey("users.id"))

    def __repr__(self) -> str:
        return f'{self.title}'


