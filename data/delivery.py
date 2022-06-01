import sqlalchemy
from data.db_session import SqlAlchemyBase


class delivery(SqlAlchemyBase):
    __tablename__ = 'delivery'

    delivery = sqlalchemy.Column(sqlalchemy.String, nullable=False, primary_key=True)
    cost = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
