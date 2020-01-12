import arrow

from tests import Birthday
from time_adapters.sqlalchemy import ArrowType


def seed(session):
    ts = arrow.now('local')

    day = Birthday(
        ts=ts,
    )
    session.add(day)
    session.commit()

    return ts


def test_basic(session, engine):
    ts = seed(session)

    assert ArrowType == Birthday.ts.property.columns[0].type.__class__

    # value in db should be in UTC
    res = engine.execute('SELECT ts FROM birthday').first()[0]
    assert str(ts.to('UTC').format('YYYY-MM-DD HH:mm:ss.SSSSSS' )) == res

    # object should be rehydrated with an arrow object and local tz
    res = session.query(Birthday).first().ts
    assert arrow.Arrow == type(res)
    assert arrow.get(ts) == res
    assert ts.tzinfo == res.tzinfo


def test_precision(session):
    ts = seed(session)

    ArrowType.PRECISION = 'second'
    res = session.query(Birthday).first().ts
    assert ts.floor('second') == res

    # reset
    ArrowType.PRECISION = 'microsecond'


def test_tz_change(session):
    ts = seed(session)

    ArrowType.TZ = 'UTC'
    res = session.query(Birthday).first().ts
    assert ts.to('UTC') == res

    # reset
    ArrowType.TZ = 'local'
