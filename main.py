from sqlalchemy import text, insert, select
from src import engine, metadata_obj, orders


metadata_obj.drop_all(engine)
metadata_obj.create_all(engine)

with engine.connect() as connection:
    stmt = insert(orders).values(
        [
            (1, 'me', 'one'),
            (2, 'you', 'two')
        ]
    )

    connection.execute(stmt)
    connection.commit()

with engine.connect() as connection:
    query = select(orders)
    result = connection.execute(query)
    print(result.scalar_one())


