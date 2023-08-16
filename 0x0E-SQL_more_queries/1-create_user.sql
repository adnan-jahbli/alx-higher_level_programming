-- A script that creates the MySQL server user user_0d_1.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to the user
GRANT ALL PRIVILEGES ON '.' TO 'user_0d_1'@'localhost';

-- Flush privileges
FLUSH PRIVILEGES;
