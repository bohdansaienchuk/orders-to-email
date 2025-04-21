from sqlalchemy import create_engine


engine = create_engine(
    url='sqlite:///database/orders.db',
    echo=True
)
