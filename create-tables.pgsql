DROP TABLE IF EXISTS departmentRecords;
DROP TABLE IF EXISTS appointmentRecords;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS departments;
DROP TABLE IF EXISTS roles;

CREATE TABLE roles
(
    roleId INT NOT NULL PRIMARY KEY,
    roleName TEXT NOT NULL
);


CREATE TABLE users
(
    userId INT NOT NULL PRIMARY KEY GENERATED ALWAYS AS IDENTITY, -- primary key column
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
    userId INT NOT NULL,
    departmentId INT NOT NULL,
    PRIMARY KEY (userId, departmentId),
    FOREIGN KEY(userId) REFERENCES users(userId) ON DELETE CASCADE,
    FOREIGN KEY(departmentId) REFERENCES departments(departmentId) ON DELETE CASCADE
);

CREATE TABLE appointmentRecords
(
    appointmentId INT NOT NULL PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    appointmentStartTime TIMESTAMP NOT NULL,
    appointmentEndTime TIMESTAMP NOT NULL,
    appointmentTopic TEXT NOT NULL,
    appointmentComment TEXT,
    userId INT NOT NULL,
    departmentId INT NOT NULL,
    FOREIGN KEY(userId) REFERENCES users(userId) ON DELETE CASCADE,
    FOREIGN KEY(departmentId) REFERENCES departments(departmentId) ON DELETE CASCADE
);
