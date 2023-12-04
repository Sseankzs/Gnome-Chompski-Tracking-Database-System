import SQL_Query as sq

    
def Show_Tables():
    sq.Show_Database()
    table = input("Which table # would you like to see?: ")
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
        
#TODO: Add LogIn and Interface
        
def main():
    sq.Show_Database()

    quit()

if __name__ == "__main__":
    main()