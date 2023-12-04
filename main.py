import SQL_Query as sq

    
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
        case 0:
            return 0
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
    quit()

if __name__ == "__main__":
    main()