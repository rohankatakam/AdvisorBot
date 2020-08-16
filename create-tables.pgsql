DROP TABLE IF EXISTS departmentRecords;
DROP TABLE IF EXISTS ticketRecords;
DROP TABLE IF EXISTS appointmentRecords;
DROP TABLE IF EXISTS facultys;
DROP TABLE IF EXISTS departments;
DROP TABLE IF EXISTS roles;
DROP TABLE IF EXISTS majors;


CREATE TABLE roles
(
    roleId INT NOT NULL PRIMARY KEY,
    roleName TEXT NOT NULL
);

CREATE TABLE faculties
(
    facultyId INT NOT NULL PRIMARY KEY GENERATED ALWAYS AS IDENTITY, -- primary key column
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password BYTEA NULL,
    salt BYTEA NOT NULL,
    roleId INT NOT NULL,
    FOREIGN KEY(roleId) REFERENCES roles(roleId) ON DELETE CASCADE
);

CREATE TABLE departments
(
    departmentId INT NOT NULL PRIMARY KEY,
    departmentName TEXT NOT NULL
);

CREATE TABLE departmentRecords
(
    facultyId INT NOT NULL,
    departmentId INT NOT NULL,
    PRIMARY KEY (facultyId, departmentId),
    FOREIGN KEY(facultyId) REFERENCES facultys(facultyId) ON DELETE CASCADE,
    FOREIGN KEY(departmentId) REFERENCES departments(departmentId) ON DELETE CASCADE
);

CREATE TABLE majors
(
    majorId INT NOT NULL PRIMARY KEY,
    majorName TEXT NOT NULL
);

CREATE TABLE appointmentRecords
(
    appointmentId INT NOT NULL PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    appointmentDate DATE NOT NULL,
    appointmentStartTime TIMESTAMP NOT NULL,
    appointmentEndTime TIMESTAMP NOT NULL,
    appointmentTopic TEXT NOT NULL,
    appointmentComment TEXT,
    facultyId INT NOT NULL,
    studentId INT,
    studentEmail TEXT NOT NULL,
    majorId INT,
    departmentId INT NOT NULL,
    FOREIGN KEY(majorId) REFERENCES majors(majorId) ON DELETE CASCADE,
    FOREIGN KEY(facultyId) REFERENCES facultys(facultyId) ON DELETE CASCADE,
    FOREIGN KEY(departmentId) REFERENCES departments(departmentId) ON DELETE CASCADE
);

CREATE TABLE ticketRecords
(
    ticketId INT NOT NULL PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    studentId INT,
    time TIMESTAMP NOT NULL,
    ticketTitle TEXT,
    ticketContent TEXT,
    solved BOOLEAN NOT NULL,
    advisorId INT NOT NULL,
    studentEmail TEXT NOT NULL,
    departmentId INT NOT NULL,
    majorId INT,
    FOREIGN KEY(majorId) REFERENCES majors(majorId) ON DELETE CASCADE,
    FOREIGN KEY(advisorId) REFERENCES facultys(facultyId) ON DELETE CASCADE,
    FOREIGN KEY(departmentId) REFERENCES departments(departmentId) ON DELETE CASCADE
);
