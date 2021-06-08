-- Ejecutar este script con el comando: cat tables.sql | mysql -uroot -p

-- database creation
CREATE DATABASE IF NOT EXISTS readIT_library;
USE readIT_library;

-- TABLES CREATION

-- Users table
CREATE TABLE IF NOT EXISTS Users (
IdUser varchar(40) NOT NULL, PRIMARY KEY(IdUser),
FirstName varchar(50) NOT NULL,
LastName varchar(50) NOT NULL,
Phone varchar(30),
Email varchar(50) NOT NULL,
Password varchar(512) NOT NULL,
City varchar(50) NOT NULL
);

-- Books table
CREATE TABLE IF NOT EXISTS Books (
IdBook varchar(40) NOT NULL, PRIMARY KEY(IdBook),
Authors varchar(256) NOT NULL,
Title varchar(256) NOT NULL,
Description varchar(512) NOT NULL,
ISBN varchar(30),
Status varchar(30) NOT NULL,
Uploaded DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL
);

-- Shared table 
CREATE TABLE IF NOT EXISTS Shared (
IdShared varchar(40) NOT NULL, PRIMARY KEY(IdShared),
IdGiver varchar(40) NOT NULL, FOREIGN KEY(IdGiver) REFERENCES Users(IdUser),	
IdReceiver varchar(40) NOT NULL, FOREIGN KEY(IdReceiver) REFERENCES Users(IdUser),
IdBook varchar(40) NOT NULL, FOREIGN KEY(IdBook) REFERENCES Books(IdBook),
Datashared DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
StatusRequest varchar(30) NOT NULL
);



