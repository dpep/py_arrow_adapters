import arrow
import pytest

from sqlalchemy.exc import InterfaceError

from tests import Birthday
from arrow_adapters.sqlalchemy import ArrowType


format_str = 'YYYY-MM-DD HH:mm:ss.SSSSSS'


def seed(session):
    ts = arrow.now('local')

    day = Birthday(
        ts=ts,
        sec=ts,
        utc=ts,
    )
    session.add(day)
    session.commit()

    return ts


def test_basic(session, engine):
    ts = seed(session)

    assert ArrowType == Birthday.ts.property.columns[0].type.__class__

    # value in db should be in UTC
    res = engine.execute('SELECT ts FROM birthday').first()[0]
    assert str(ts.to('UTC').format(format_str)) == res

    # object should be rehydrated with an arrow object and local tz
    res = session.query(Birthday).first().ts
    assert arrow.Arrow == type(res)
    assert arrow.get(ts) == res
    assert ts.tzinfo == res.tzinfo


def test_precision(session):
    ts = seed(session)

    res = session.query(Birthday).first().sec
    assert ts.floor('second') == res


def test_tz_change(session):
    ts = seed(session)

    res = session.query(Birthday).first().utc
    assert ts.to('UTC') == res

    ArrowType.DEFAULT_TZ = 'UTC'
    res = session.query(Birthday).first().ts
    assert ts.to('UTC') == res

    # reset
    ArrowType.DEFAULT_TZ = 'local'


def test_query(session):
    ts = seed(session)

    res = session.query(Birthday).filter(
        Birthday.ts == ts,
    ).first().ts
    assert ts == res


    res = session.query(Birthday).filter(
        Birthday.ts == str(ts),
    ).first().ts
    assert ts == res


def test_sqlite_adapter(session, engine):
    ts = seed(session)

    assert 'pysqlite' == engine.driver

    def query():
        return engine.execute(
            'SELECT ts FROM birthday WHERE ts = :t', t=ts
        ).first()[0]


    with pytest.raises(InterfaceError):
        query()


    # load sqlite adapter
    import arrow_adapters.sqlite
    assert ts.to('UTC').format(format_str) == query()
