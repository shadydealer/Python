from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import (Column, String, Integer,
                        Float, ForeignKey, Date,
                        Time)
from sqlalchemy.orm import (sessionmaker,
                            relationship
                            )

Base = declarative_base()


class Movie(Base):
    __tablename__ = "Movies"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    rating = Column(Float, nullable=False)

class Projection(Base):

    __tablename__ = "Projections"
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey("Movies.id"), nullable=True)
    type = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    movie = relationship("Movie", backref="projections")

class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    salt = Column(String, nullable=False)


class Reservation(Base):

    __tablename__ = "Reservations"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("Users.id"), nullable=False)
    projection_id = Column(Integer, ForeignKey(
        "Projections.id"), nullable=False)
    row = Column(Integer, nullable=False)
    col = Column(Integer, nullable=False)
    user = relationship("User", backref="reservations")

engine = create_engine("sqlite:///cinema2.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
