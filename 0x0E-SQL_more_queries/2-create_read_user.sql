-- A script that creates the database hbtn_0d_2 and the user user_0d_2.

-- creating hbtn_0d_2 database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- creating user_0d_2
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Giving SELECT privilege to user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
