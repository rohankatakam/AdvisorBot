DROP TABLE IF EXISTS department_records;
DROP TABLE IF EXISTS ticket_records;
DROP TABLE IF EXISTS appointment_records;
DROP TABLE IF EXISTS faculties;
DROP TABLE IF EXISTS majors;
DROP TABLE IF EXISTS departments;
-- DROP TABLE IF EXISTS roles;


-- CREATE TABLE roles
-- (
--     roleid INT NOT NULL PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
--     rolename TEXT NOT NULL
-- );

CREATE TABLE faculties
(
    facultyid INT NOT NULL PRIMARY KEY GENERATED ALWAYS AS IDENTITY, -- primary key column
    username TEXT NOT NULL UNIQUE,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password BYTEA NULL,
    salt BYTEA NOT NULL
    -- roleid INT NOT NULL,
    -- FOREIGN KEY(roleid) REFERENCES roles(roleid) ON DELETE CASCADE
);

CREATE TABLE departments
(
    departmentid INT NOT NULL PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    departmentname TEXT NOT NULL
);

CREATE TABLE department_records
(
    facultyid INT NOT NULL,
    departmentid INT NOT NULL,
    PRIMARY KEY (facultyid, departmentid),
    FOREIGN KEY(facultyid) REFERENCES faculties(facultyid) ON DELETE CASCADE,
    FOREIGN KEY(departmentid) REFERENCES departments(departmentid) ON DELETE CASCADE
);

CREATE TABLE majors
(
    majorid INT NOT NULL PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    majorname TEXT NOT NULL,
    departmentid INT NOT NULL,
    FOREIGN KEY(departmentid) REFERENCES departments(departmentid) ON DELETE CASCADE
);

CREATE TABLE appointment_records
(
    appointmentid INT NOT NULL PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    appointmentdate TEXT NOT NULL,
    appointmentstarttime TEXT NOT NULL,
    appointmentendtime TEXT,
    appointmenttopic TEXT NOT NULL,
    appointmentcomment TEXT,
    facultyid INT NOT NULL,
    studentid INT,
    studentfirstname TEXT NOT NULL,
    studentlastname TEXT NOT NULL,
    studentemail TEXT NOT NULL,
    majorid INT,
    departmentid INT NOT NULL,
    FOREIGN KEY(majorid) REFERENCES majors(majorid) ON DELETE CASCADE,
    FOREIGN KEY(facultyid) REFERENCES faculties(facultyid) ON DELETE CASCADE,
    FOREIGN KEY(departmentid) REFERENCES departments(departmentid) ON DELETE CASCADE
);

CREATE TABLE ticket_records
(
    ticketid INT NOT NULL PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    studentid INT,
    time TEXT NOT NULL,
    tickettitle TEXT,
    ticketcontent TEXT,
    solved BOOLEAN NOT NULL,
    advisorid INT NOT NULL,
    studentfirstname TEXT NOT NULL,
    studentlastname TEXT NOT NULL,
    studentemail TEXT NOT NULL,
    departmentid INT NOT NULL,
    majorid INT,
    FOREIGN KEY(majorid) REFERENCES majors(majorid) ON DELETE CASCADE,
    FOREIGN KEY(advisorid) REFERENCES faculties(facultyid) ON DELETE CASCADE,
    FOREIGN KEY(departmentid) REFERENCES departments(departmentid) ON DELETE CASCADE
);
