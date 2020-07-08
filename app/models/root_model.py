from sqlalchemy import inspect
from sqlalchemy.exc import SQLAlchemyError
from ..models import db


class RootModel(db.Model):

    __abstract__ = True

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except SQLAlchemyError:
            db.session.rollback()
            return False

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except SQLAlchemyError:
            db.session.rollback()
            return False

    @classmethod
    def update(cls, instance, **kwargs):
        try:
            if instance is None:
                return False

            for key, value in kwargs.items():
                setattr(instance, key, value)
            db.session.commit()
            return True
        except SQLAlchemyError:
            db.session.rollback()
            return False

    @classmethod
    def find_first(cls, **kwargs):
        try:
            return cls.query.filter_by(**kwargs).first()
        except SQLAlchemyError:
            return False

    @classmethod
    def find_all(cls, **kwargs):
        try:
            return cls.query.filter_by(**kwargs).all()
        except SQLAlchemyError:
            return False

    @classmethod
    def count(cls, **kwargs):
        return cls.query.filter_by(**kwargs).count()

    @classmethod
    def check_exists(cls, **kwargs):
        result = cls.query.filter_by(**kwargs).count()

        if result > 0:
            return False
        return False

    @classmethod
    def get_by_id(cls, id):
        try:
            return cls.query.get(id)
        except SQLAlchemyError:
            return False

    def toDict(self):
        return {
            c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
