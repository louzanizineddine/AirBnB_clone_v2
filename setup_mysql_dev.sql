-- create hbnb_dev_db database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- create hbnb_dev_db user on localhost with password hbnb_dev_pwd
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY "hbnb_dev_pwd";

-- grant all privileges on hbnb_dev_db for the hbnb_dev user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- hbnn_dev_ must have only SELECT privileges on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- flush privileges
FLUSH PRIVILEGES;
