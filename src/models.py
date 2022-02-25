import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

association_table = Table('personaje_favorito', Base.metadata,
    Column('usuario_id', ForeignKey('usuario.id')),
    Column('personaje_id', ForeignKey('personaje.id'))
)

association_table = Table('planeta_favorito', Base.metadata,
    Column('usuario_id', ForeignKey('usuario.id')),
    Column('planeta_id', ForeignKey('planeta.id'))
)


class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre_de_usuario = Column(String(250), nullable=False)
    contrasena = Column(String(250), nullable=False)
    personaje = relationship("Personaje",
                    secondary=association_table)
    planeta = relationship("Planeta",
                    secondary=association_table)


class Personaje(Base):
    __tablename__ = 'personaje'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre_de_personaje = Column(String(100), nullable=False)
    pelicula = Column(String(100), nullable=False)
    especie = Column(String(50), nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship(Usuario)


class Planeta(Base):
    __tablename__ = 'planeta'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre_de_planeta = Column(String(50), nullable=False)
    poblacion = Column(Integer, nullable=False)
    clima = Column(String(30), nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship(Usuario)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')