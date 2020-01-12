import pytest
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from tests import Base


@pytest.fixture
def engine():
    """Create a new db for each test."""
    return create_engine('sqlite:///:memory:')


@pytest.fixture
def session(engine):
    session = sessionmaker(bind=engine)()
    Base.metadata.create_all(engine)

    yield session

    Base.metadata.drop_all(engine)
    session.close()
