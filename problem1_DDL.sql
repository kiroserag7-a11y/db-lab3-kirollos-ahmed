DROP DATABASE IF EXISTS company;
CREATE DATABASE company;
USE company;

-- 1. Create DEPARTMENT table
CREATE TABLE DEPARTMENT (
    Dnumber INT NOT NULL,
    Dname VARCHAR(50) NOT NULL,
    mgr_ssn INT,
    mgr_start_date DATE,
    PRIMARY KEY (Dnumber)
);

-- 2. Create EMPLOYEE table
CREATE TABLE EMPLOYEE (
    ssn INT NOT NULL,
    fname VARCHAR(30) NOT NULL,
    lname VARCHAR(30) NOT NULL,
    bdate DATE,
    address VARCHAR(100),
    gender CHAR(1),
    salary DECIMAL(10,2),
    Dno INT,
    PRIMARY KEY (ssn),
    FOREIGN KEY (Dno) REFERENCES DEPARTMENT(Dnumber)
);

-- 3. Add foreign key for DEPARTMENT (mgr_ssn points to EMPLOYEE)
ALTER TABLE DEPARTMENT 
ADD FOREIGN KEY (mgr_ssn) REFERENCES EMPLOYEE(ssn);

-- 4. Create PROJECT table
CREATE TABLE PROJECT (
    Pnumber INT NOT NULL,
    Pname VARCHAR(50) NOT NULL,
    Plocation VARCHAR(50),
    Dno INT,
    PRIMARY KEY (Pnumber),
    FOREIGN KEY (Dno) REFERENCES DEPARTMENT(Dnumber)
);