from arrow import Arrow
from psycopg2.extensions import adapt, register_adapter


# register Arrow type with postgres
register_adapter(
    Arrow,
    lambda x: adapt(x.to('UTC').datetime)
)

# http://initd.org/psycopg/docs/advanced.html#adapting-new-python-types-to-sql-syntax
