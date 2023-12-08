import SQL_Query as sq
import time
import os


clear = lambda: os.system('cls')

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
    
def Show_Tables():
    
    sq.Show_Database()
    table = int(input("Which table # would you like to see? (3 does not work): "))
    while table < 0 or table > 4:
        print("Please choose from the available table #")
        sq.Show_Database()
        table = int(input("Which table # would you like to see? (3 does not work): "))
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
    # Add if else statements for choices
    
        
def Add_Tuples():
    clear()
    sq.Show_Database()
    table = int(input("Which table # would you like to add to?: "))
    while table < 1 or table > 4:
        print("Please choose from the available table #")
        sq.Show_Database()
        table = int(input("Which table # would you like to see?: "))
    match table:
        case 0:
            return
        case 1:
            sq.Add_Employees()
        case 2:
            sq.Add_Chompskis()
        case 3:
            sq.Add_Oversees()
        case 4:
            sq.Add_Swarms()
        
def Delete_Tuples():
    clear()
    sq.Show_Database()
    table = int(input("Which table # would you like to add to?: "))
    while table < 1 or table > 4:
        print("Please choose from the available table #")
        sq.Show_Database()
        table = int(input("Which table # would you like to see?: "))
    match table:
        case 0:
            return
        case 1:
            sq.Delete_Employees()
        case 2:
            sq.Delete_Chompskis()
        case 3:
            sq.Delete_Oversees()
        case 4:
            sq.Delete_Swarms()
            
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
        case 2:
            sq.Search_Chompskis()
        case 3:
            sq.Search_Oversees()
        case 4:
            sq.Search_Swarms()

def menu():
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
        while action != 0:
            while action < 1 or action > 6:
                print("Invalid action, please choose from the menu below")
                action = menu()
            match action:
                case 1:
                    Show_Tables()
                    break
                case 2:
                    Add_Tuples()
                    break
                case 3:
                    Delete_Tuples()
                    break
                case 4:
                    Search_Tuples()
                    break
                case 5:
                    Increase_Biodiversity()
                    break
                case 0:
                    quit()
            
#TODO: Add LogIn and Interface


        
def main():


    Initial_setup()
    
    menu()

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