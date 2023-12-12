import SQL_Query as sq
import time
import os


clear = lambda: os.system('cls')

authorization_lists = ('Intern', 'Employee', 'Supervisor', 'Bossman')

def Initial_setup():  
    SQLstatus = open("SQL_Status.txt", "r")
    if SQLstatus.mode == 'r':
        status = SQLstatus.read()
        if status != "1":
            print("Initializing Entities")
            sq.Populate_All()
            
            SQLstatus = open("SQL_Status.txt","w+")
            
            SQLstatus.write("1")
            time.sleep(1)
            print("Entities Initialized")
            
            
#TODO: Change to increase biodiversity
def Populate_Table():
    
    tables = ["Employees", "Swarms", "Chompskis", "Oversees"]
    
    if any(not sq.Is_Populated(tables)):
        populate_condition = ['Y', 'y', 'N', 'n', 'q', 'Q']
        while populate in populate_condition:
            populate = input("Would you like to populate the entity? (Data populated is entirely 'random')[y/n/q(quit)]:")
            if populate == "Y" or populate == "y":
                for i in tables:
                    print("{}. Populate {}",(tables.index(i) + 1,i))
                    x += 1
                print("5. Populate All Entities")
                print("6. I change my mind (back)")
                while option < 0 or option > 6:
                    option = int(input("Which entity would you like to populate?"))
                for x in range (0,5):
                    if not sq.Is_Populated(tables.x):
                        sq.Populate(tables.option)
                    else:
                        print("Entity has been populated")
                if option == 5:
                    sq.Populate_All()
    else: 
        print("All entities have been populated")
        return          
    
def Show_Tables():
    clear()
    sq.Show_Database()
    table = int(input("Which table # would you like to see? (enter 0 to quit): "))

    while table < 0 or table > 4:
        print("Please choose from the available table #")
        sq.Show_Database()
        table = int(input("Which table # would you like to see? (enter 0 to quit): "))
    match table:
        case 0:
            clear(  )
            return
        case 1:
            sq.Show_Employees()
            okay = input("press ENTER")
            Show_Tables()
        case 2:
            sq.Show_Chompskis()
            okay = input("press ENTER")
            Show_Tables()
        case 3:
            sq.Show_Oversees()
            okay = input("press ENTER")
            Show_Tables()
        case 4:
            sq.Show_Swarms()
            okay = input("press ENTER")
            Show_Tables()
        case 0:
            return 0
    # Add if else statements for choices
    
        
def Add_Tuples():
    clear()
    sq.Show_Database()
    table = int(input("Which table # would you like to add to? [0 to exit]: "))
    
    while table < 0 or table > 4:
        print("Please choose from the available table #")
        sq.Show_Database()
        table = int(input("Which table # would you like to see?: "))
    match table:
        case 0:
            return
        case 1:
            fname = input("Please enter a first name: ")
            mname = input("Please enter a middle name: ")
            lname = input("Please enter a last name: ")
            password = input("Plase enter a password: ")
            if password != 0:
                authorization_no = 5
                count = 0
                for i in authorization_lists:
                    count +=1
                    print( "{}. ".format(count) + i)
                while authorization_no not in range(0,4):
                    authorization_no = int(input("Please enter authorization number:"))
                
                sq.Add_Employees(fname, mname, lname, password, authorization_no)
                
            Add_Tuples()
        case 2:
            age = int(input("Please enter Chompski age: "))
            name = input("Please enter Chompski name: ")
            height = float(input("Please enter Chompskis height: "))
            weight = float(input("Please enter Chompski weight: "))
            no_teeth = int(input("Please enter number of teeth: "))
            print("Swarm id, Quantity")
            sq.Show_Quantity()
            swarm_id = int(input("Please enter swarm_id: "))
            sq.Add_Chompski(age, name, height, weight, no_teeth, swarm_id)
            Add_Tuples()

        case 3:
            sq.Show_Oversees()
            emp_id = int(input("Enter employee ID: "))
            swarm_id = int(input("Enter swarm id: "))
            sq.Add_Oversees(emp_id, swarm_id)
            Add_Tuples()
        case 4:
            name = input("Enter swarm name: ")
            latitude = float(input("Enter latitude: "))
            longitude = float(input("Enter longitude: "))
            sq.Add_Swarm(name, latitude, longitude)
            
            Add_Tuples()
        case 0:
            return
    
        
def Delete_Tuples():
    clear()
    sq.Show_Database()
    table = int(input("Which table # would you like to delete?: "))
    while table < 0 or table > 4:
        print("Please choose from the available table #")
        sq.Show_Database()
        table = int(input("Which table # would you like to delete?: "))
    match table:
        case 0:
            return
        case 1:
            print("Example conditions:")
            print("'Employee_id = 2 AND lname = benjamin'")
            print("Join conditions with 'AND' or 'OR'")
            condition = input("Enter your condition for deletion: ")
            sq.Delete_Employee(condition)
            Delete_Tuples()
        case 2:
            print("Example conditions:")
            print("'chompskis_id = 2 AND name = poopy'")
            print("Join conditions with 'AND' or 'OR'")
            condition = input("Enter your condition for deletion: ")
            print()
            sq.Delete_Chompski(condition)

            Delete_Tuples()
        case 3: 
            print("Example conditions:")
            print("'employee_id = 12 AND employee_id = 12'")
            print("Join conditions with 'AND' or 'OR'")
            condition = input("Enter your condition for deletion: ")
            sq.Delete_Oversees(condition)
            Delete_Tuples()
        case 4:
            print("Example conditions:")
            print("'swarm_id = 2 AND name = Goopy'")
            print("Join conditions with 'AND' or 'OR'")
            condition = input("Enter your condition for deletion: ")
            sq.Delete_Swarm(condition)
            Delete_Tuples()
            
def Search_Tuples():
    clear()
    sq.Show_Database()
    table = int(input("Which table # would you like to search?: "))
    while table < 0 or table > 4:
        print("Please choose from the available table #")
        sq.Show_Database()
        table = int(input("Which table # would you like to search?: "))
    match table:
        case 0:
            menu()
        case 1:
            sq.Search("Employee")
            Search_Tuples()
        case 2:
            sq.Search("Gnome_Chompskis")
            Search_Tuples()
        case 3:
            sq.Search("Oversees")
            Search_Tuples()
        case 4:
            sq.Search("Swarm")
            Search_Tuples()

def Show_Max():
    sq.Show_Database()
    table_no = int(input("Which table would you like to choose: "))
    while table_no < 0 or table_no > 4:
        print("Please choose from the available table #")
        table_no = int(input("Which table would you like to choose: "))
        sq.Show_Database()
        
    match table_no:
        case 0:
            Show_Max()
        case 1:
            table = "employee"
        case 2:
            table = "gnome_chompskis"
        case 3:
            table = "oversees"
        case 4:
            table = "swarm"
    sq.Show_Attributes(table)
    attribute = input("Which attribute would you like to see?: ")
    sq.Show_Max(attribute, table)

def Show_Min():
    sq.Show_Database()
    table_no = int(input("Which table would you like to choose: "))
    while table_no < 0 or table_no > 4:
        print("Please choose from the available table #")
        table_no = int(input("Which table would you like to choose: "))
        sq.Show_Database()
        
    match table_no:
        case 0:
            Show_Min()
        case 1:
            table = "employee"
        case 2:
            table = "gnome_chompskis"
        case 3:
            table = "oversees"
        case 4:
            table = "swarm"
    sq.Show_Attributes(table)
    attribute = input("Which attribute would you like to see?: ")
    sq.Show_Min(attribute, table)

def Show_Avg():
    sq.Show_Database()
    table_no = int(input("Which table would you like to choose: "))
    while table_no < 0 or table_no > 4:
        print("Please choose from the available table #")
        table_no = int(input("Which table would you like to choose: "))
        sq.Show_Database()
        
    match table_no:
        case 0:
            Show_Avg()
        case 1:
            table = "employee"
        case 2:
            table = "gnome_chompskis"
        case 3:
            table = "oversees"
        case 4:
            table = "swarm"
    sq.Show_Attributes(table)
    attribute = input("Which attribute would you like to see?: ")
    sq.Show_Avg(attribute, table)
    
def Swarm_Functions():
    clear()
    print("------Choose your actions------")
    print("1. Average Quantity\t\t\t2. Sort by Quantity (Ascending)")
    print("3. Sort by Quantity (Descending)\t\t4. Swarm Quantity")
    print("5. Update Swarm Location")
    choice = int(input("Choose one:"))
    while choice < 0 or choice > 5:
        print("Invalid input")
        choice = int(input("Choose one:"))
    match choice:
        case 0:
            return
        case 1:
            sq.Show_Avg_Quantity()
            Swarm_Functions()
        case 2:
            sq.Show_Quantity_Asce()
            Swarm_Functions()
        case 3:
            sq.Show_Quantity_Desc()
            Swarm_Functions()
        case 4:
            sq.Show_Quantity()
            Swarm_Functions()
        case 5:
            sq.Update_Location()
            Swarm_Functions()
            

def menu():
    sq.login()
    action = 1
    clear()
    while action != 0:
        print("-----------Welcome to the Gnome Chompski Tracking Database System-----------")
        print("Choose your actions:")
        print("1. Display Tables\t\t\t2. Add Tuples")
        print("3. Delete Tuples\t\t\t4. Search Tuples")
        print("5. Swarm Functions \t\t\t6. Show Max")
        print("7. Show Min\t\t\t\t8. Show Average")
        print("9. Update Password")
        print("0. Quit")
        action = int(input(""))
        while action < 0 or action > 10:
            print("Invalid action, please choose from the menu below")
            ok = input("press ENTER")
            action = menu()
        match action:
            case 1:
                Show_Tables()
                menu()
            case 2:
                Add_Tuples()
                menu()
            case 3:
                Delete_Tuples()
                menu()
            case 4:
                Search_Tuples()
                menu()
            case 5:
                Swarm_Functions()
                menu()
            case 6:
                Show_Max()
                menu()
            case 7:
                Show_Min()
                menu()
            case 8:
                Show_Avg()
                menu()
            case 9:
                clear()
                sq.Update_Password()
                menu()
            case 0:
                quit()
            
#TODO: Add LogIn and Interface


        
def main():
    Initial_setup()
    menu()

if __name__ == "__main__":
    main()