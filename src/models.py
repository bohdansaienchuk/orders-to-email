from sqlalchemy import Table, Column, Integer, String, MetaData


metadata_obj = MetaData()

orders = Table(
    'orders',
    metadata_obj,
    Column('order_id', Integer, primary_key=True),
    Column('name', String),
    Column('surname', String)
)