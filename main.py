from pathlib import Path
import os


def read_files_folders():
    path = Path("")
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1}. {items}")

def create_file():
    try:
        read_files_folders()

        print()
        name = input("Enter your file name : ")
        p = Path(name)
        if not p.exists():
            with open(p, 'w') as fs:
                data = input("Enter your data in file :")
                fs.write(data)
                print()
                
            print("FILE CREATED SUCCESFULLY")
        else:
            print("FILE ALREADY EXISTS")

    except Exception as error:
        print(F"AN ERROR IS OCCURED AS {error}")

    print()
    print()

def read_file():
    try: 
        read_files_folders()
        print("")
        name = input("Enter your file name : ")
        print("")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                show_data = fs.read()
                print("--------------------------- FILE DATA -------------------------------------")
                print(show_data)
                print("")
            print("FILE READED SUCCESFULLY.")
            print("")
        else:
            print("NO SUCH FILE EXISTS IN THIS FOLDER")
            print("")
    
    except Exception as error:
        print(F"AN ERROR IS OCCURED AS {error}")
    
    print("")
    print("")
    
def update_file():
    try:
        read_files_folders()
        print("")
        name = input("Enter your file name : ")
        print("")
        p = Path(name)
        if p.exists() and p.is_file():
            print("=============== OPERATIONS ================")
            print("1. Do you want to update file name")
            print("2. Do you want to overwrite the data of file")
            print("3. Do you want to append some content in your file ")
            print("")

            choice = int(input("Enter your choice : "))
            print("")

            if choice == 1:
                name_2 = input("Enter your new File name : ")
                p2 = Path(name_2)
                p.rename(p2)
                print("")
                print("FILE NAME UPDATED SUCCESFULLY")
                print("")
            
            elif choice == 2:
                with open(p, 'w') as fs:
                    overwrite_data = input("Enter your data you want to overwrite : ")
                    print("--------------------------- FILE DATA -------------------------------------")
                    fs.write(overwrite_data)
                    print("DATA OVERWRITE SUCCESFULLY")
            
            elif choice == 3:
                with open(p, 'a') as fs:
                    append_data = input("Enter your data you want to append : ")
                    fs.write(" " + append_data)
                    print("DATA APPENDED SUCCESFULLY")
        else:
                print("NO SUCH FILE EXISTS IN THIS FOLDER")
                print("")
    
    except Exception as error:
        print(F"AN ERROR IS OCCURED AS {error}")

    print("")
    print("")

def delete_file():
    try:
        read_files_folders()

        print("")
        name = input("Enter your file name :")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print("FILE DELETED SUCCESFULLY.")
        else:
            print("FILE DIRECTORY IS NOT FOUND")

    except Exception as error:
        print(f"An error is occured as {error}")
    print()
    print()


while True:
    print("")
    print("=============== MENU ================")
    print("1. Creating a File.")
    print("2. Reading a File.")
    print("3. Updating a File.")
    print("4. Deleting a File.")
    print("5. Exist")
    print("")


    option = int(input("Enter your Option : "))

    if option == 1:
        create_file()

    elif option == 2:
        read_file()

    elif option == 3:
        update_file()
    
    elif option == 4:
        delete_file()
    else:
        break
