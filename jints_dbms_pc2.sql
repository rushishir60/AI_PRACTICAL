-- 🌟 SQL PRACTICAL : Joins, Subquery and View 🌟

-- Create Database
CREATE DATABASE CollegeDB;
USE CollegeDB;

-- Create Tables
CREATE TABLE Department(
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);

CREATE TABLE Course(
    course_id INT PRIMARY KEY,
    course_name VARCHAR(50),
    dept_id INT
);

CREATE TABLE Student(
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    course_id INT,
    marks INT
);

-- Insert Sample Data
INSERT INTO Department VALUES (1, 'Computer Science'), (2, 'Data Science');
INSERT INTO Course VALUES (101, 'DBMS', 1), (102, 'AI', 1), (201, 'ML', 2);
INSERT INTO Student VALUES (1, 'Rushikesh', 101, 85), (2, 'Amit', 102, 90), (3, 'Sneha', 201, 88);

-- 1. INNER JOIN
SELECT s.student_name, c.course_name
FROM Student s
INNER JOIN Course c ON s.course_id = c.course_id;

-- 2. LEFT JOIN
SELECT s.student_name, c.course_name
FROM Student s
LEFT JOIN Course c ON s.course_id = c.course_id;

-- 3. SUBQUERY (students above average marks)
SELECT student_name, marks
FROM Student
WHERE marks > (SELECT AVG(marks) FROM Student);

-- 4. SUBQUERY with IN
SELECT student_name
FROM Student
WHERE course_id IN (SELECT course_id FROM Course WHERE dept_id = 1);

-- 5. CREATE VIEW and USE IT
CREATE VIEW Student_View AS
SELECT s.student_name, c.course_name, s.marks
FROM Student s JOIN Course c ON s.course_id = c.course_id;

SELECT * FROM Student_View WHERE marks > 80;
