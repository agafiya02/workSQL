import sqlalchemy
from .session import SqlAlchemyBase, SerializerMixin


class Departments(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'departments'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    chief = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    members = sqlalchemy.Column(sqlalchemy.String,
                                sqlalchemy.ForeignKey("users.id"))
    email = sqlalchemy.Column(sqlalchemy.String, nullable=True)
