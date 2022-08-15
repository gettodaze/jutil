"""References:
https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html
https://docs.sqlalchemy.org/en/14/orm/tutorial.html
https://docs.sqlalchemy.org/en/14/core/engines.html#sqlite
"""
import typing as tp

from sqlalchemy import Column, ForeignKey, Integer, Table, create_engine, inspect
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy.sql.schema import Column


class _Base:
    @classmethod
    def get_columns(cls) -> tp.Tuple[Column, ...]:
        return tuple(inspect(cls).columns)

    def __repr__(self) -> str:
        items = ((c.name, getattr(self, c.name)) for c in self.get_columns())
        inner = ", ".join(f"{k}={v}" for k, v in items)
        return f"{self.__class__.__name__}({inner})"


Base = declarative_base(cls=_Base)


class Parent(Base):
    __tablename__ = "parent"
    id = Column(Integer, primary_key=True)
    children = relationship("Child")


class Child(Base):
    __tablename__ = "child"
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey("parent.id"))
    parent = relationship("Parent", back_populates="children")


engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)()

# fmt: off
from IPython import embed; embed() # JTODO: remove
# fmt: on
