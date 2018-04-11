from sqlalchemy.orm import relationship, backref, joinedload
from sqlalchemy import Column, DateTime, String, Integer, Float, ForeignKey, func

from base import Base, inverse_relationship, create_tables

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)

    url = Column(String, unique=True)
    name = Column(String)
    diameter = Column(Integer)
    gravity = Column(String)
    population = Column(Integer)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def parse_json(self, json_data):
        self.url = json_data['url']
        self.name = json_data['name']
        self.diameter = json_data['diameter']
        self.gravity = json_data['gravity']
        self.population = json_data['population']

class Person(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)

    url = Column(String, unique=True)
    name = Column(String)
    gender = Column(String)
    height = Column(Integer)
    mass = Column(Integer)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def parse_json(self, json_data):
        self.url = json_data['url']
        self.name = json_data['name']
        self.gender = json_data['gender']
        self.height = json_data['height']
        self.mass = json_data['mass']


class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)

    url = Column(String, unique=True)
    name = Column(String)
    model = Column(String)
    manufacturer = Column(String)
    cost_in_credits = Column(Integer)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def parse_json(self, json_data):
        self.url = json_data['url']
        self.name = json_data['name']
        self.model = json_data['model']
        self.manufacturer = json_data['manufacturer']

        if json_data["cost_in_credits"]=="unknown":
            self.cost_in_credits = 0
        else:
            self.cost_in_credits = json_data['cost_in_credits']


class Starship(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)

    url = Column(String, unique=True)
    name = Column(String)
    model = Column(String)
    manufacturer = Column(String)
    cost_in_credits = Column(Integer)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def parse_json(self, json_data):
        self.url = json_data['url']
        self.name = json_data['name']
        self.model = json_data['model']
        self.manufacturer = json_data['manufacturer']

        if json_data["cost_in_credits"]=="unknown":
            self.cost_in_credits = 0
        else:
            self.cost_in_credits = json_data['cost_in_credits']

class Species(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)

    url = Column(String, unique=True)
    name = Column(String)
    classification = Column(String)
    designation = Column(String)
    skin_colors = Column(String)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def parse_json(self, json_data):
        self.url = json_data['url']
        self.name = json_data['name']
        self.classification = json_data['classification']
        self.designation = json_data['designation']
        self.skin_colors = json_data['skin_colors']

if __name__ != '__main__':
    create_tables()
