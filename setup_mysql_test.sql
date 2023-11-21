-- create hbnb_test_db database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- create hbnb_test_db user on localhost with password hbnb_dev_pwd
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- grant all privileges on hbnb_test_db for the hbnb_test user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- hbnn_dev_ must have only SELECT privileges on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- flush privileges
FLUSH PRIVILEGES;
