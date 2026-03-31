from files import *

def show_memu():
    print("\n----FILES ----")
    print("1. Make registers")
    print("2. Read register")
    print("3. Look for ID.")
    print("4. Uptade register")
    print("5. Delete register")
    print("6. Export for CSV")
    print("7. Exit")


def give_datas():
    name = input("Get it the name: ")
    age =  int(input("Get it the age: "))
    status = input("Get it the status (active or unactive): ")
    ID = int(input("Get it ID: "))
    course = input("Get it the course: ")

    return{
        "name": name,
        "age": age,
        "status": status,
        "ID":ID,
        "course": course
    }


if __name__== "__main__":
    option = ""

    
    while option != "7":
        show_memu()
        option = input("pick up option: ")


        if option == "1":
            datas = give_datas()
            maker_register(datas)
            print("Registers has saved in JSON.")

        elif option == "2":
            registers = read_registers_json()
            print("\n---- Registers found it ----")
            if not registers:
                print("It has not resgisters.")
            else:
                for r in registers:
                    print(r)

        elif option == "3":
            id_vaule = input("Get it the ID the register: ")
            register = look_for__id(id_vaule, "ID")

            if register:
                print("\nRegister found it:")
                print(register)
            else:
                print("Register not foun it")
        
        

        elif option == "4":
            
            id_vaule = input("Get it the ID the register: ")
            new_datas =give_datas()

            updated = update_register(id_vaule, "ID",new_datas)

            if updated:
                print("Register has been updated.")

            else:
                print("Data do not find it ")

        elif option == "5":
            id_vaule = input("Get it the ID the register: ")
            
            deleted = delete_register_json(id_vaule, "ID")

            if deleted:
                print("Register has been deleted.")

            else:
                print("Data do not find it ")

        elif option =="6":
            export_for_csv()



        elif option == "7":
            print("See you later.")

        else:
            print("Option unvalible")
