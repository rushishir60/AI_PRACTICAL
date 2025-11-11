CREATE DATABASE
college;
USE college;
CREATE TABLE student (
roll_no INT PRIMARY KEY
AUTO_INCREMENT, name
VARCHAR(50),
age INT,
dept VARCHAR(50)
);
INSERT INTO student
(name,age,dept)
VALUES ('Rutuja',20,'AI&DS'),
 ('Priya',21,'Comp');
SELECT * FROM student;
UPDATE student SET age=22 WHERE name='Priya';
DELETE FROM student WHERE roll_no=2;
CREATE VIEW v_stud AS SELECT name,dept FROM student;
CREATE INDEX idx_name ON student(name); 


select *from student;

