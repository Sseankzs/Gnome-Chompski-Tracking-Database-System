import mysql.connector
import random
from enum import Enum

db = mysql.connector.connect(
    host= "localhost",
    user= "Ssean",
    password = "Ssean",
    database = "GenCorp"

)

mycursor = db.cursor()

authorization_list = ('Intern', 'Employee', 'Supervisor')


class Authorizations(Enum):
    INTERN = "Intern",
    EMPLOYEE = "Employee",
    SUPERVISOR = "Supervisor",
    BOSSMAN = "Bossman"
    
#Login function
def login():
    found = 0
    while found == 0:
        id = input("Please enter your employee ID (enter 0 to quit): ")
        if id == '0':
            quit()
        mycursor.execute("SELECT * FROM Employee WHERE employee_id = (%s)", (id,))
        for x in mycursor:
            found += 1
        if found == 0:
            print("That Employee ID does not exist. Please enter a valid ID or scram!")
    
    correct = 0
    while correct == 0:
        pswd = input("Please enter your password (enter 0 to quit): ")
        if pswd == '0':
            quit()
        mycursor.execute("SELECT * FROM Employee WHERE employee_id = (%s) AND password = (%s)", (id, pswd))
        for x in mycursor:
            correct += 1
        if correct == 0:
            print("That password is not correct. Enter the correct password or scram!")

#Showers
def Show_Employees():
    print("(E_id, Fname, Mname, Lname, Password, Authorization)")
    mycursor.execute("SELECT * FROM Employee")
    for x in mycursor:
        print(x)

def Show_Chompskis():
    print("age, name, height, weight, no. of teeth, swarm_id")
    mycursor.execute("SELECT * FROM Gnome_Chompskis")
    for x in mycursor:
        print(x)

def Show_Swarms():
    print("s_id, name, longitude, latitude")
    mycursor.execute("SELECT * FROM Swarm")
    for x in mycursor:
        print(x)
        
def Show_Oversees():
    print("e_id, s_id")
    mycursor.execute("SELECT * FROM Oversees")
    for x in mycursor:
        print(x)

def Show_Database():
    mycursor.execute("SHOW tables")
    i = 1
    for x in mycursor:  
        print("Table #{}: {}".format(i, x)), 
        i += 1

def Show_Quantity():
    mycursor.execute("SELECT swarm_id, COUNT(swarm_id) as quantity FROM gnome_chompskis group by swarm_id")
    print("swarm_id, quantity")
    for x in mycursor:
        print(x)
    cont = input("press ENTER")
    
def Show_Max(max : str, table : str):
    mycursor.execute(f"SELECT MAX({max}) FROM {table}")
    for x in mycursor:
        print(x)
    ok = input("press ENTER")

def Show_Min(min : str, table : str):
    mycursor.execute(f"SELECT MIN({min}) FROM {table}")
    for x in mycursor:
        print(x)
    ok = input("press ENTER")

def Show_Avg(avg : str, table : str):
    mycursor.execute(f"SELECT AVG({avg}) FROM {table}")
    print(f"average {avg}:")
    for x in mycursor:
        print(x)
    ok = input("press ENTER")
    
def Show_Avg_Quantity():
    mycursor.execute("SELECT swarm.swarm_id, COUNT(gnome_chompskis.swarm_id) as quantity FROM swarm JOIN gnome_chompskis ON swarm.swarm_id = gnome_chompskis.swarm_id GROUP BY swarm.swarm_id")
    print("Swarm_id, Quantity")
    for x in mycursor:
        print(x)
    ok = input("press ENTER")

def Show_Quantity_Desc():
    mycursor.execute("SELECT swarm.swarm_id, COUNT(gnome_chompskis.swarm_id) as quantity FROM swarm JOIN gnome_chompskis ON swarm.swarm_id = gnome_chompskis.swarm_id GROUP BY swarm.swarm_id ORDER BY quantity DESC")
    print("Swarm_id, Quantity")
    for x in mycursor:
        print(x)
    ok = input("press ENTER")

def Show_Quantity_Asce():
    mycursor.execute("SELECT swarm.swarm_id, COUNT(gnome_chompskis.swarm_id) as quantity FROM swarm JOIN gnome_chompskis ON swarm.swarm_id = gnome_chompskis.swarm_id GROUP BY swarm.swarm_id ORDER BY quantity ASC")
    print("Swarm_id, Quantity")
    for x in mycursor:
        print(x)
    ok = input("press ENTER")

def Show_Attributes(table_name):
    mycursor.execute("SHOW COLUMNS FROM {}".format(table_name))
    print("Attributes")
    for x in mycursor:
        print(x)
    
#Getters (TODO: nothing yet)
def Get_Authorization(employee_id : int):
    authorization = mycursor.execute(
        "SELECT authorization FROM Employee WHERE employee_id = {}".format(employee_id))
    return authorization

def Is_Populated(table_name):
    mycursor.execute(f'SELECT COUNT(*) FROM {table_name}')
    return mycursor.fetchone()[0] > 0

def Add_Oversees(Emp_id, Swarm_id):
    mycursor.execute("INSERT INTO Oversees(employee_id, swarm_id) VALUES(%s, %s)", (Emp_id, Swarm_id))
    db.commit()
    print("Insertion succesful")
    choice = input("Oversees updated [press ENTER]")


def Add_Employees(fname, mname, lname, password, authorization_no):
    authorization = authorization_list[authorization_no - 1]

    try:
        mycursor.execute("INSERT INTO Employee(fname, mname, lname, password, authorization)VALUES(%s,%s,%s,%s,%s)", (fname, mname, lname, password, authorization))
        db.commit()
    except mysql.connector.IntegrityError as err:
        print("Error: {}".format(err))
        
    print("Employee Added Succesfully")
    print("Updated Employee Table:")
    print("(E_id, Fname, Mname, Lname, Password, Authorization)")
    mycursor.execute("SELECT * FROM Employee")
    print("The insertion was succesful!")    
    for x in mycursor:
        print(x)
    choice = input("Database Updated [press ENTER]")
    if choice == 1:
        db.commit()

def Add_Swarm(name : str, latitude : float, longitude : float):
    try:
        mycursor.execute("INSERT INTO Swarm(name, latitude, longitude)VALUES(%s,%s,%s)",(name,latitude,longitude))
        db.commit()
    except mysql.connector.IntegrityError as err:
        print("Error: {}".format(err))
    
    print("Swarm Added Successfully")
    print("Updated Swarm Table:")
    print("(s_id, name, latitude, longitude)")
    mycursor.execute("SELECT * FROM Swarm")
    print("The insertion was succesful!")
    for x in mycursor:
        print(x)
    choice = input("Database Updated [press ENTER]")
    if choice == 1:
        db.commit()
    

def Add_Chompski(age : int, name : str, height : float, weight : float, no_teeth : int, swarm_id : int):
    try: 
        mycursor.execute("INSERT Gnome_Chompskis(age, name, height, weight, no_teeth, swarm_id)VALUES(%s,%s,%s,%s,%s,%s)", (age, name, height, weight, no_teeth, swarm_id))
        db.commit()
    except mysql.connector.IntegrityError as err:
        print("Error: {}".format(err))
        return err
    
    mycursor.execute("SELECT * FROM Gnome_Chompskis")
    for x in mycursor:
        print(x)
    choice = input("Database Updated [press ENTER]")
    if choice == 1:
        db.commit()
    
#Removers (TODO:)
def Delete_Employee(condition : str):
    try:
        mycursor.execute("DELETE FROM Employee WHERE {}".format(condition))
        db.commit()
    except mysql.connector.errors.IntegrityError or mysql.connector.errors.ProgrammingError as err:
        print(err)
        ok = input("press ENTER")
        return err
    mycursor.execute("SELECT * FROM Employee")
    for x in mycursor:
        print(x)
    choice = input("Database updated [press ENTER]")


def Delete_Oversees(condition: str):
    try:
        mycursor.execute("DELETE FROM oversees WHERE {}".format(condition))
        db.commit
        mycursor.execute("SELECT * FROM oversees")
        for  x in mycursor:
            print(x)
        ok = input("Database updated [press ENTER]")
    except mysql.connector.errors.IntegrityError or mysql.connector.errors.ProgrammingError as er:
        print(er)
        ok = input("press ENTER")
    
    
            
def Delete_Swarm(condition : str):
    try: 
        mycursor.execute("DELETE FROM Swarm WHERE {}".format(condition))
        db.commit()
        mycursor.execute("SELECT * FROM Swarm")
        for x in mycursor:
            print(x)
    except mysql.connector.errors.IntegrityError or mysql.connector.errors.ProgrammingError as err:
        print("Error: Condition does not exist. {}".format(err))
        ok = input("press ENTER")
    

def Delete_Chompski(condition : str):
    try:
        mycursor.execute("DELETE FROM Gnome_Chompski WHERE {}".format(condition))
        db.commit()
        mycursor.execute("SELECT * FROM Gnome_Chompski")
        for x in mycursor:
            print(x)
    except mysql.connector.errors.ProgrammingError as err:
        print("Error: Condition does not exist. {}".format(err))
        ok = input("press ENTER")
        
#Updaters (TODO: Update_Authorization, Update_Swarm )
def Update_Password():
    found = 0
    while found == 0:
        id = input("Please enter your employee ID (enter 0 to quit): ")
        if id == '0':
            quit()
        try:
            mycursor.execute(f"SELECT * FROM Employee WHERE employee_id = {id}")
            for x in mycursor:
                found += 1
        except:
            print("wrong password")
        if found == 0:
            print("That Employee ID does not exist. Please enter a valid ID or scram!")
            ok = input("press ENTER")
    
    correct = 0
    while correct == 0:
        pswd = input("Please enter your current password (enter 0 to quit): ")
        if pswd == '0':
            quit()
        mycursor.execute(f"SELECT * FROM Employee WHERE employee_id = {id} AND password = {pswd}")
        for x in mycursor:
            correct += 1
        if correct == 0:
            print("That password is not correct. Enter the correct password or scram!")
            ok = input("press ENTER")

    while correct == 1:
        new_pswd = input("Please enter your new password (enter 0 to quit): ")
        if new_pswd == '0':
            quit()
        else:
            mycursor.execute(f"UPDATE employee SET password = '{new_pswd}' WHERE employee_id = {id} AND password = {pswd}")
            db.commit()
            print("Changes Saved")
            mycursor.execute(f"SELECT * FROM employee WHERE employee_id = {id}")
            for x in mycursor:
                print(x)
            ok = input("press ENTER")
            correct += 1
    
def Update_Location():
    swarm_exists = 0
    while swarm_exists == 0:
        s_id = input("Please enter the swarm id: ")
        mycursor.execute("SELECT * FROM Swarm WHERE swarm_id = (%s)", (s_id,))
        for x in mycursor:
            swarm_exists += 1
        if swarm_exists >= 1:
            lat = input("Please enter the new latitude for the swarm: ")
            long = input("Please enter the new longitude for the swarm: ")
            mycursor.execute("UPDATE Swarm SET latitude = (%s), longitude = (%s) WHERE swarm_id = (%s)", (lat, long, s_id))
            db.commit()
    print("Location  Updated")
    Show_Swarms()
    ok = input("press ENTER")


        
 #Search (TODO: Search_Chompski, Search_Employee, Search_Swarm, Search_Oversees)
def Search(table_name : str):
    mycursor.execute("SHOW COLUMNS FROM {}".format(table_name))
    print("Attributes")
    for x in mycursor:
        print(x)
    Conditions = input("Attributes to search (employee_id = 5 OR/AND fname = 'john'): ")
    try:
        mycursor.execute(f"SELECT * FROM {table_name} WHERE {Conditions}")
        for x in mycursor:
            print(x)
            ok = input("press ENTER")
    except mysql.connector.errors.ProgrammingError as er:
        print(er)
        print("note: conditions that are variable type VARCHAR might require a single quote ['']")
        ok = input("press ENTER")
        
#Initial Set Ups (TODO: Populate Oversees)
def Populate_All():
    Populate_Employee()
    Populate_Swarm()
    Populate_Gnome_Chompskis()
    Populate_Oversees()

def Create_DB():
    mycursor.execute("CREATE DATABASE GenCorp")

def Create_Tables():
    mycursor.execute("CREATE TABLE Employee (employee_id int PRIMARY KEY NOT NULL AUTO_INCREMENT,fname VARCHAR(50) NOT NULL, mname VARCHAR(50),lname VARCHAR(50) NOT NULL, password VARCHAR(50) NOT NULL, authorization ENUM('Intern','Employee', 'Supervisor', 'Bossman'))")
    mycursor.execute("CREATE TABLE Swarm (swarm_id int PRIMARY KEY AUTO_INCREMENT, name varchar(45) NOT NULL, latitude double(9, 5), longitude double (9,5))")
    mycursor.execute("CREATE TABLE Oversees (employee_id int, swarm_id int, FOREIGN KEY(employee_id) REFERENCES Employee(employee_id),  FOREIGN KEY(swarm_id) REFERENCES Swarm(swarm_id))")
    mycursor.execute("CREATE TABLE Gnome_Chompskis (chompskis_id int PRIMARY KEY AUTO_INCREMENT,name varchar(45) NOT NULL,  age smallint, height double(10,2), weight double (10,2), no_teeth int UNSIGNED, swarm_id int, FOREIGN KEY(swarm_id) REFERENCES Swarm(swarm_id))")
    print("Tables created")

def Populate(table):
    if table == "Employee":
        Populate_Employee()
    elif table == "Swarm":
        Populate_Swarm()
    elif table == "Oversees":
        Populate_Oversees()
    elif table == "Gnome_Chompskis":
        Populate_Gnome_Chompskis()

def Populate_Employee():
    fname_list = ('James', 'Gabe', 'Jamal', 'Rudolf', 'Chuck', 'Evan', 'Benjamin', 'Nathan', 'Sean')
    lname_list = ('Weiss', 'Weeks', 'Moody', 'Holland', 'Buck', 'Picks', 'Bradford', 'Simpsons', 'Sanchez')
    authorization_list = ('Intern', 'Employee', 'Supervisor')

    for _ in range(10):
        fname = random.choice(fname_list)
        lname = random.choice(lname_list)
        authorization = random.choice(authorization_list)
        mycursor.execute("INSERT INTO Employee(fname, lname, password, authorization)VALUES (%s, %s, 'password', %s)", (fname,lname,authorization))
        db.commit()
    print("Succesfully Populated")
    print("Employee_id, First name, Middle name, Last name, Password, Authorization")
    mycursor.execute("SELECT * FROM Employee")
    for x in mycursor:
        print(x)

def Populate_Swarm():
    names = ('Goopy' , 'Poopy', 'Danger', 'Hostile', 'Tame', 'Lame', 'DBDB', 'GenCorp Specialty', 'Anything', 'Friendly', 'Woopy')
    for x in range(10):
        latitude = random.uniform(-180.0,180.0)
        longitude = random.uniform(-180.0,180.0)
        mycursor.execute("INSERT INTO Swarm(name, latitude, longitude)VALUES(%s,%s,%s)",(names[x],latitude,longitude))
        db.commit()
    
    mycursor.execute("SELECT * FROM Swarm")
    for x in mycursor:
        print(x)

def Populate_Oversees():
    for n in range(1, 11):  
        mycursor.execute("INSERT INTO Oversees(employee_id, swarm_id)VALUES(%s, %s)", (n, n))
    db.commit()
        
        
    mycursor.execute("SELECT * FROM Oversees")
    for x in mycursor:
        print(x)

def Populate_Gnome_Chompskis():
    
    for x in range (100):
        mycursor.execute("INSERT INTO Gnome_Chompskis(age, name, height, weight, no_teeth, swarm_id)VALUES(%s,%s,%s,%s,%s,%s)", (random.randint(1,100), 'Chompy{}'.format(x), random.uniform(10.0,50.0), random.uniform(10.0,250.0),random.randint(24,312), random.randint(1,10)))
    db.commit()
    
    mycursor.execute("SELECT * FROM Gnome_Chompskis")
    for x in mycursor:
        print(x)
        
