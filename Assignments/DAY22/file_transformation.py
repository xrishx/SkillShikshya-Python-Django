import os

def make_dir():
    name = input("Enter the name of your directory: ")
    try:
        os.mkdir(name)
        print(f"Directory {name} successfully created")
        print(f"You are now inside {name} directory")
    except FileExistsError:
        print(f"Directory {name} already exists here.")
    return name

def make_file(folder):
    name = input("Enter the name of your file (dont forget the *.txt) : ")
    try:    
        with open(name, "x") as file:
            print(f"File {name} successfully created!")

    except FileExistsError:
        print(f"File {name} already exists")
        main()

def read_file(name):
    with open(name, "r") as file:
        content = file.read()
        print(content)
    print("\n ------End of File------")

def get_info():
    pass

def delete_file():
    pass

def main():
    folder = ""
    path = ""
    print("""
        print("1. Make a Directory")
        print("2. Make a File Inside the Directory")
        print("3. Write Text to the File")
        print("4. Read the File")
        print("5. Update (Append) Text Without Overwriting")
        print("6. Get Current Directory and File Path")
        print("7. Get File Name and Size")
        print("8. Get File Extension")
        print("9. Delete the File")
        print("0. Exit")
        """)
    choice = input("What would you like to do! - ")
