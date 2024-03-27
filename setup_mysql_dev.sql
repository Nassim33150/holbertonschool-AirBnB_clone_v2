-- If the the database hbnb_dev_db does not exist, create the database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- If the user does not exist, create the user and grant all privileges
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd'; 
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schéma.* TO 'hbnb_dev'@'localhost';
