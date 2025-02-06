from sqlalchemy import create_engine
from models import Base

engine = create_engine('sqlite:///socmed.sqlite', echo=True)

Base.metadata.drop_all(engine)

Base.metadata.create_all(engine)