# pip install mysql-connector-python
import mysql.connector


#pip show mysql-connector-python

# CREATE DATABASE college;
# USE college;

# CREATE TABLE student (
#     roll_no INT PRIMARY KEY,
#     name VARCHAR(50),
#     marks INT
# );


#python path

# Connect to MySQL Database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",   # replace with your MySQL password
    database="college"
)
 
cursor = con.cursor()

# --- Functions ---
def add_student():
    roll = int(input("Enter Roll No: "))
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))
    cursor.execute("INSERT INTO student VALUES (%s, %s, %s)", (roll, name, marks))
    con.commit()
    print("✅ Record added successfully!\n")

def view_students():
    cursor.execute("SELECT * FROM student")
    rows = cursor.fetchall()
    print("\n--- Student Records ---")
    for r in rows:
        print(r)
    print()

def update_student():
    roll = int(input("Enter Roll No to Update: "))
    marks = int(input("Enter New Marks: "))
    cursor.execute("UPDATE student SET marks=%s WHERE roll_no=%s", (marks, roll))
    con.commit()
    print("✅ Record updated successfully!\n")

def delete_student():
    roll = int(input("Enter Roll No to Delete: "))
    cursor.execute("DELETE FROM student WHERE roll_no=%s", (roll,))
    con.commit()
    print("✅ Record deleted successfully!\n")

# --- Menu ---
while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    ch = input("Enter choice: ")

    if ch == '1':
        add_student()
    elif ch == '2':
        view_students()
    elif ch == '3':
        update_student()
    elif ch == '4':
        delete_student()
    elif ch == '5':
        break
    else:
        print("❌ Invalid choice. Try again!\n")

# Close connection
con.close()
