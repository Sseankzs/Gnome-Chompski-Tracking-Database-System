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
    table = int(input("Which table # would you like to see? (3 does not work, enter 0 to quit): "))

    while table < 0 or table > 4:
        print("Please choose from the available table #")
        sq.Show_Database()
        table = int(input("Which table # would you like to see? (3 does not work, enter 0 to quit): "))
    match table:
        case 0:
            clear(  )
            return
        case 1:
            sq.Show_Employees()
            Show_Tables()
            clear()
        case 2:
            sq.Show_Chompskis()
            Show_Tables()
            clear()
        case 3:
            sq.Show_Oversees()
            Show_Tables()
            clear()
        case 4:
            sq.Show_Swarms()
            Show_Tables()
            clear()
        case 0:
            return 0
    # Add if else statements for choices
    
        
def Add_Tuples():
    clear()
    sq.Show_Database()
    table = int(input("Which table # would you like to add to?: "))
    
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
            swarm_id = int(input("Please enter swarm_id: "))
            sq.Add_Chompskis(age, name, height, weight, no_teeth, swarm_id)
            Add_Tuples()

        case 3:
            emp_id = int(input("Enter employee ID: "))
            swarm_id = int(input("Enter swarm id: "))
            sq.Add_Oversees(emp_id, swarm_id)
            Add_Tuples()
        case 4:
            name = input("Enter swarm name: ")
            latitude = float("Enter latitude: ")
            longitude = float("Enter longitude: ")
            sq.Add_Swarms(name, latitude, longitude)
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
            sq.Delete_Employees(condition)
            Delete_Tuples()
        case 2:
            print("Example conditions:")
            print("'chompskis_id = 2 AND name = poopy'")
            print("Join conditions with 'AND' or 'OR'")
            condition = input("Enter your condition for deletion: ")
            print()
            sq.Delete_Chompskis(condition)
            Delete_Tuples()
        case 3:
            print("Example conditions: 'employee_id = 2 AND swarm_id = poopy'")
            print("Join conditions with 'AND' or 'OR'")
            condition = input("Enter your condition for deletion: ")
            sq.Delete_Oversees(condition)
            Delete_Tuples()
        case 4:
            print("Example conditions:")
            print("'swarm_id = 2 AND name = Goopy'")
            print("Join conditions with 'AND' or 'OR'")
            condition = input("Enter your condition for deletion: ")
            sq.Delete_Swarms(condition)
            Delete_Tuples()
            
def Search_Tuples():
    clear()
    sq.Show_Database()
    table = int(input("Which table # would you like to delete from?: "))
    while table < 1 or table > 4:
        print("Please choose from the available table #")
        sq.Show_Database()
        table = int(input("Which table # would you like to see? (3 does not work): "))
    match table:
        case 0:
            return
        case 1:
            sq.Search_Employees()
            Search_Tuples()
        case 2:
            sq.Search_Chompskis()
            Search_Tuples()
        case 3:
            sq.Search_Oversees()
            Search_Tuples()
        case 4:
            sq.Search_Swarms()
            Search_Tuples()

def menu():
    #sq.login()
    action = 1
    clear()
    while action != 0:
        print("-----------Welcome to the Gnome Chompski Tracking Database System-----------")
        print("Choose your actions:")
        print("1. Display Tables\t\t\t2. Add Tuples")
        print("3. Delete Tuples\t\t\t4. Search Tuples")
        print("5. Increase Biodiversity")
        print("0. Quit")
        action = int(input(""))
        while action < 0 or action > 6:
            print("Invalid action, please choose from the menu below")
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
                Increase_Biodiversity()
                menu()
            case 0:
                quit()
            
#TODO: Add LogIn and Interface


        
def main():
    Initial_setup()
    menu()


    '''
    action = int(menu())
    while action != 0:
        while action < 1 or action > 7:
            print("Invalid action, please choose from the menu below")
            action = menu()
        match action:
            case 1:
                Show_Tables()
            case 2:
                Increase_Biodiversity()
            case 3:
                sq.Add_Employees()
            case 4:
                sq.Add_Swarm()
            case 5:
                sq.Add_Chompskis()
            case 6:
                sq.Add_Overseers()
            case 7:
                sq.Update_Location()
            case 0:
                quit()
    quit()
    '''

if __name__ == "__main__":
    main()