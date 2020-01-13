from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from time_adapters.sqlalchemy import ArrowType


Base = declarative_base()


class Birthday(Base):
    __tablename__ = 'birthday'

    ts = Column(ArrowType,  primary_key=True)
    sec = Column(ArrowType(precision='second'))
    utc = Column(ArrowType(tz='UTC'))
