USE company;

-- Insert EMPLOYEES
INSERT INTO EMPLOYEE (ssn, fname, lname, bdate, address, gender, salary, Dno) VALUES
(101, 'Ahmed', 'Ali', '1990-05-15', 'Cairo, Egypt', 'M', 8000.00, NULL),
(102, 'Mona', 'Hassan', '1995-08-20', 'Alexandria, Egypt', 'F', 9500.00, NULL),
(103, 'Omar', 'Khaled', '1992-12-10', 'Giza, Egypt', 'M', 7000.00, NULL);

-- Insert DEPARTMENTS
INSERT INTO DEPARTMENT (Dnumber, Dname, mgr_ssn, mgr_start_date) VALUES
(1, 'HR', 101, '2020-01-01'),
(2, 'IT', 102, '2021-03-15'),
(3, 'Finance', 103, '2022-06-01');

-- Update Employee Dno
UPDATE EMPLOYEE SET Dno = 1 WHERE ssn = 101;
UPDATE EMPLOYEE SET Dno = 2 WHERE ssn = 102;
UPDATE EMPLOYEE SET Dno = 3 WHERE ssn = 103;

-- Insert PROJECTS
INSERT INTO PROJECT (Pnumber, Pname, Plocation, Dno) VALUES
(10, 'Website Redesign', 'Alexandria', 2),
(20, 'Payroll System', 'Cairo', 3),
(30, 'Recruitment Drive', 'Giza', 1);