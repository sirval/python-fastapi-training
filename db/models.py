from db.database import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String

class DbUser(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    