import mysql.connector
import random
from enum import Enum

db = mysql.connector.connect(
    host= "localhost",
    user= "Ssean",
    passwd = "Ssean",
    database = "GenCorp"
)

mycursor = db.cursor()

class Authorizations(Enum):
    INTERN = "Intern",
    EMPLOYEE = "Employee",
    SUPERVISOR = "Supervisor",
    BOSSMAN = "Bossman"
    

#Getters
def Describe_Database():
    mycursor.execute("SHOW tables")
    for x in mycursor:
        print(x)
    

def Describe_Tables(Table : str):
    mycursor.execute("DESCRIBE {}".format(Table))
    for x in mycursor:
        print(x)
        
def Get_Authorization(employee_id : int):
    authorization = mycursor.execute(
        "SELECT authorization FROM Employee WHERE employee_id = {}".format(employee_id))
    return authorization

#Adders
def Add_Employees(fname, mname, lname, password, authorization : str):
    if not isinstance(authorization,Authorizations):
        raise TypeError('authorization must be an instance of Authorizations Enum')
    mycursor.execute("INSERT INTO Employees(fname, mname, lname, password, authorization)VALUES(%s,%s,%s,%s,%s)", (fname, mname, lname, password, authorization))
    db.commit()
    
    print("Employee Added Succesfully")
    print("Updated Employee Table:")
    mycursor.execute("SELECT * FROM Employee")
    for x in mycursor:
        print(x)

def Add_Swarm(name : str, latitude : float, longitude : float):
    try:
        mycursor.execute("INSERT INTO Swarm(name, latitude, longitude)VALUES(%s,%s,%s)",(name,latitude,longitude))
        db.commit()
    except  mysql.connector.IntegrityError as err:
        print("Error: {}".format(err))
    

def Add_Chompskis(age : int, name : str, height : float, weight : float, no_teeth : int, swarm_id : int):
    try: 
        Chompskis = "INSERT Gnome_Chompski(age, name, height, weight, no_teeth, swarm_id)VALUES(%s,%s,%s,%s,%s,%s)", (age, name, height, weight, no_teeth, swarm_id)
        mycursor.execute(Chompskis)
        quantity = mycursor.execute("SELECT COUNT (*) FROM Gnome_Chompskis WHERE swarm_id = %s", (swarm_id))
        mycursor.execute("UPDATE Swarm SET quantity = %s WHERE swarm_id = %s", (quantity,swarm_id))
        db.commit()   
    except mysql.connector.IntegrityError as err:
        print("Error: {}".format(err))
    
    mycursor.execute("SELECT * FROM Gnome_Chompski")
    for x in mycursor:
        print(x)
    
#Removers
def Delete_Swarm(condition : str):
    mycursor.execute("DELETE FROM Swarm WHERE {}".format(condition))
    db.commit()
    mycursor.execute("SELECT * FROM Swarm")
    for x in mycursor:
        print(x)

#Initial Set Ups
def Create_Tables():
    mycursor.execute("CREATE TABLE Employee (employee_id int PRIMARY KEY NOT NULL AUTO_INCREMENT,fname VARCHAR(50) NOT NULL, mname VARCHAR(50),lname VARCHAR(50) NOT NULL, password VARCHAR(50) NOT NULL, authorization ENUM('Intern','Employee', 'Supervisor', 'Bossman'))")
    mycursor.execute("CREATE TABLE Swarm (swarm_id int PRIMARY KEY AUTO_INCREMENT, quantity int, latitude double(9, 5), longitude double (9,5))")
    mycursor.execute("CREATE TABLE Oversees (employee_id int, swarm_id int, FOREIGN KEY(employee_id) REFERENCES Employee(employee_id),  FOREIGN KEY(swarm_id) REFERENCES Swarm(swarm_id))")
    mycursor.execute("CREATE TABLE Gnome_Chompskis (chompskis_id int PRIMARY KEY AUTO_INCREMENT,name varchar(45) NOT NULL,  age smallint, name VARCHAR(50), height double(10,2), weight double (10,2), no_teeth int UNSIGNED, swarm_id int, FOREIGN KEY(swarm_id) REFERENCES Swarm(swarm_id))")
    print("Tables created")

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
    for _ in range(10):  
        mycursor.execute("SELECT")
        
        
    mycursor.execute("SELECT * FROM Oversees")
    for x in mycursor:
        print(x)

def Populate_Gnome_Chompskis():
    
    for x in range (100):
        mycursor.execute("INSERT INTO Gnome_Chompskis(age, name, height, weight, no_teeth, swarm_id)VALUES(%s,%s,%s,%s,%s,%s)", (random.randint(1,100), 'Chompy{}'.format(x), random.uniform(10.0,50.0), random.uniform(10.0,250.0),random.randint(24,312), random.randint(0,10)))
    db.commit()
    
    mycursor.execute("SELECT * FROM Gnome_Chompskis")
    for x in mycursor:
        print(x)
        
