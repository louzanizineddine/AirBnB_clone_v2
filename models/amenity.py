#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """The Amenities of a place"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship(
            'Place', secondary='place_amenity', back_populates="amenities")
