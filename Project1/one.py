import mysql.connector

connection = mysql.connector.connect(
    host="localhost",       
    user="root",         
    password="123456", 
    database="demo_user" 
)

cursor = connection.cursor()

def createTable():
    cursor.execute("""create table employee_data(
                        emp_id int unsigned auto_increment primary key ,
                        emp_name varchar(40) not null,
                        join_date date,
                        salary bigint unsigned,
                        experience int unsigned 
                        );""")
    print("Table employee_data created.")


def createEmployee():
    cursor.execute("""
        insert into employee_data
        (emp_name,join_date,salary,experience)
        values("kamal","2022-09-15",18500,1);
    """)
    connection.commit()
    print("Table employee added.")

def read_employees():
    cursor.execute("SELECT * FROM employee_data")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def delete_employee():
    cursor.execute("""
 delete from employee_data where emp_id = 10;
""")
    connection.commit()
    print("Employee deleted!")

def update_employee():
    cursor.execute("""
  update employee_data set salary = 50000 where emp_id= 2;
""")
    connection.commit()
    print("Employee updated!")

# createTable()
# createEmployee()
# read_employees()
# delete_employee()
# update_employee()




