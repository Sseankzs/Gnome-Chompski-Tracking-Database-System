import SQL_Query as sq
import time
import os


def Initial():  
    SQLstatus = open("SQL_Status.txt", "r")
    if SQLstatus.mode == 'r':
        status = SQLstatus.read()
        if status != "1" or "2":
            print("Initializing Entities")
            sq.Create_DB()
            sq.Create_Tables()
            
            SQLstatus = open("SQL_Status.txt","w+")
            
            SQLstatus.write("1")
            time.sleep(1)
            print("Entities Initialized")
            
            Populate_Table(status)

    
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
    sq.Show_Database()
    table = int(input("Which table # would you like to see? (3 does not work): "))
    while table < 1 or table > 4:
        print("Please choose from the available table #")
        sq.Show_Database()
        table = int(input("Which table # would you like to see? (3 does not work): "))
    match table:
        case 1:
            sq.Show_Employees()
        case 2:
            sq.Show_Chompskis()
        case 3:
            sq.Show_Oversees()
        case 4:
            sq.Show_Swarms()
    # Add if else statements for choices
    
    
def Increase_Biodiversity(employee_id):
    if sq.Get_Authorization(employee_id) == 2:
        while new != "s" or new != "c":
            new = input("Do you want to add a new swarm or Chompski? [s/c]")
            if new == "s":
                sq.Add_Swarm()
            elif new == "c":
                sq.Add_Chompskis()
    else:
        print("you do not have acces to this function")
        
def menu():
    print("-----------Welcome to the Gnome Chompski Tracking Database System-----------")
    print("Choose your actions:")
    print("1. Display Tables\t\t\t2. Increase BioDiversity")
    print("3. Add Employees\t\t\t4. Add Swarms")
    print("5. Add Chompskis\t\t\t6. Assign Overseers")
    print("0. Quit")
    action = input("")
    return action
            
#TODO: Add LogIn and Interface
        
def main():
    
    creds = sq.check_logged_in()
    
    if len(creds) == 0:
        sq.sql_login()
        sq.connect()
        print("logged in")
    else:
        sq.connect()
        print("you have connected")
    

    
    '''
    action = int(menu())
    while action != 0:
        while action < 1 or action > 6:
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
            case 0:
                quit()
    quit'''

if __name__ == "__main__":
    main()