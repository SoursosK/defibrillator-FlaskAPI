CREATE TABLE Defibrillator(
    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    lat varchar(15),
    long varchar(15),
    name varchar(40),
    description varchar(400),
    problemType varchar(50),
    problemDescription varchar(1000),
    photo blob DEFAULT NULL
);

CREATE TABLE User(
    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username varchar(15),
    password varchar(30),
    userType varchar(20)
);