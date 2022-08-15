from sqlalchemy import Column, ForeignKey, Integer, Table, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()


class Parent(Base):
    __tablename__ = "parent"
    id = Column(Integer, primary_key=True)
    children = relationship("Child")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, children={self.children})"


class Child(Base):
    __tablename__ = "child"
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey("parent.id"))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, parent_id={self.parent_id})"


engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)()

# fmt: off
from IPython import embed; embed() # JTODO: remove
# fmt: on
