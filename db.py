"""Db models definition module"""
from sqlalchemy import Column, String
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Widget(db.Model):
    __tablename__ = "widgets"
    name = Column(String(120), primary_key=True, nullable=False)
    description = Column(String(1000))

    def __repr__(self):
        return f"{self.name}"

    def to_dict(self):
        return {name: value for name, value
                in self.__dict__.items() if name in self.__table__.columns}
