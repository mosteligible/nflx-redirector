DROP DATABASE IF EXISTS TEST_DB;

CREATE DATABASE IF NOT EXISTS TEST_DB;

CREATE TABLE TEST_TABLE
(
    Title varchar(250),
    ReleaseDate datetime NOT NULL,
    Type varchar(250),
    Rating varchar(50),
    Quality varchar(100),
    Starring varchar(500),
    Category varchar(500),
    Runtime varchar(50),
    NetflixId varchar(10),
    Language varchar(50),
    Description varchar(2500),
    PRIMARY KEY (NetflixId)
);
