-- A script that creates the database hbtn_0d_usa
-- and the table states (in the database hbtn_0d_usa)
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;

-- Switching to hbtn_0d_usa database
USE `hbtn_0d_usa`;

-- Creating the table states inside hbtn_0d_usa database
CREATE TABLE IF NOT EXISTS `states` (
	`id` INT AUTO_INCREMENT PRIMARY KEY,
	`name` VARCHAR(256) NOT NULL
);
