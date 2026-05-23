-- Creates database hbtn_0d_2 and user user_0d_2 with SELECT privilege

-- Create database if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create user if not exists
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant only SELECT privilege on hbtn_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Apply changes
FLUSH PRIVILEGES;
