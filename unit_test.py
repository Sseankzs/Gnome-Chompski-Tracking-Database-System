import unittest as ut
import SQL_Query as sq

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
        
        
if __name__ == "__main__":
    ut.main()