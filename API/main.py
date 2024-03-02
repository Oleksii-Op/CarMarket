from Database_model import create
from sqlalchemy import create_engine
from conn_to_database import select_database
from insert_new_user import create_newuser

while True:
    option = input("Please select an option: [Create a database] [Interact with database] [Exit]]\n: ")
    if option.lower() == "create a database":
        try:
            engine = create()
            print("Database created")
        except:
            print("Something went wrong")
            break
    elif option == "Interact with database":
        while True:
            interaction = input("Please select an option: [Create a user] [Delete a user] [Exit]]")
            if interaction.lower() == "create a user":
                create_newuser(engine)
            elif interaction.lower() == "delete a user":
                pass
            elif interaction.lower() == "exit":
                break
            else:
                print("Invalid option")
    elif option == "Exit":
        break
    else:
        print("Invalid option")
