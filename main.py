import SQL_Query as sq

    
def Describe_Tables():
    sq.Describe_Database()
    table = input("Which table would you like to see?: ")
    sq.Describe_Tables(table)
    
    
def Increase_Biodiversity(employee_id):
    if sq.get_Authorization(employee_id) == 2:
        while new != "s" or new != "c":
            new = input("Do you want to add a new swarm or Chompski? [s/c]")
            if new == "s":
                sq.Add_Swarm()
            elif new == "c":
                sq.Add_Chompski
    else:
        print("you do not have acces to this function")
        
def main():
    Describe_Tables()
    quit()

if __name__ == "__main__":
    main()