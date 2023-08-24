from sqlalchemy.orm import declarative_base


Base = declarative_base()

# SCHEMA
class User(Base):
    __tablename__ = 'user'
    pass