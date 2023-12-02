import mysql.connector

db = mysql.connector.connect(
    host= "localhost",
    user= "Ssean",
    passwd = "Ssean",
    database = "GenCorp"
)

mycursor = db.cursor()


def Get_Authorization(employee_id : int):
    authorization = mycursor.execute("SELECT authorization FROM Employee WHERE employee_id = " + employee_id)
    return authorization 

def Describe_Tables(Table : str):
    mycursor.execute("DESCRIBE " + Table)
    for x in mycursor:
        print(x)
    
    
def Create_Tables():
    mycursor.execute("CREATE TABLE Employee (employee_id int PRIMARY KEY AUTO_INCREMENT,fname VARCHAR(50) NOT NULL, mname VARCHAR(50),lname VARCHAR(50) NOT NULL, password VARCHAR(50) NOT NULL, authorization smallint NOT NULL)")
    mycursor.execute("CREATE TABLE Swarm (swarm_id int PRIMARY KEY AUTO_INCREMENT, quantity int, latitude double(9, 5), longitude double (9,5))")
    mycursor.execute("CREATE TABLE Oversees (employee_id int, swarm_id int, FOREIGN KEY(employee_id) REFERENCES Employee(employee_id),  FOREIGN KEY(swarm_id) REFERENCES Swarm(swarm_id))")
    mycursor.execute("CREATE TABLE Gnome_Chompskis (chompskis_id int PRIMARY KEY, age smallint, name VARCHAR(50), height double(10,2), weight double (10,2), no_teeth int UNSIGNED, swarm_id int, FOREIGN KEY(swarm_id) REFERENCES Swarm(swarm_id))")
    print("Tables created")
