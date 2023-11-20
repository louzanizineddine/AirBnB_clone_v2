#!/usr/bin/python3
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base, BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    __engine = None
    __session = None

    classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }

    def __init__(self):

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if (getenv('HBNB_ENV') == 'test'):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls)
        return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}
        # """Returns a dictionary of models currently in storage"""
        # dic = {}
        # if cls:
        #     for row in self.__session.query(cls).all():
        #         key = f"{DBStorage.classes[cls]}.{row.id}"
        #         dic[key] = row
        # # else:
        # #     for k, v in DBStorage.classes.items():
        # #         print(self.__session.query(v))
        # #         for row in self.__session.query(v).all():
        # #             key = f"{v}.{row.id}"
        # #             dic[key] = row
        # return dic

    def new(self, obj):
        """Adds new object to the storage"""
        print("a new object is to be added")
        self.__session.add(obj)

    def save(self):
        """Saves storage to database"""
        print("a new object is to be saved")
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object from database"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Loads storage dictionary from database"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))
