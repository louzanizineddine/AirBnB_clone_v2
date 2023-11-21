#!/usr/bin/pyton3

"""Unittest for DBStorage class"""

import unittest
import pep8
from os import getenv
import json

import MySQLdb
from models.base_model import BaseModel
from models.engine.db_storage import DBStorage
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review


@unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', "DB storage being used")
class TestDBStorage(unittest.TestCase):
    """testing db storage"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        
            # Connect to the MySQL database using the environment variables
        cls.db = MySQLdb.connect(getenv('HBNB_MYSQL_HOST'),
                                    getenv('HBNB_MYSQL_USER'),
                                    getenv('HBNB_MYSQL_PWD'),
                                    getenv('HBNB_MYSQL_DB'))
            
        # Create a cursor object to execute SQL queries
        cls.cursor = cls.db.cursor()
            
        # Create an instance of the DBStorage class
        cls.storage = DBStorage()            

        # Reload the storage to load all the data from the database
        cls.storage.reload()
    
    @classmethod
    def tearDownClass(cls):
        """teardown for test"""            
        # Close the connection to the database and the cursor
        cls.cursor.close()
    
    def test_pep8_DBStorage(self):
        """pep8 test"""
            
        # Check for pep8 conformance
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                             "Found code style errors (and warnings).")
    

if __name__ == "__main__":
    unittest.main()