import os

def make_dir():
    name = input("Enter directory name to create: ")
    try:
        os.mkdir(name)
        print(f"Directory '{name}' created successfully.")
    except FileExistsError:
        print(f"Directory '{name}' already exists.")

def make_file():
    name = input("Enter directory name where file should be created: ")
    if not os.path.exists(name):
        print("Directory doesn't exist. Please create it first.")
        main()
    file_name = input("Enter the file name (don't forget the *.txt): ")
    file_path = os.path.join(name, file_name)
    try:
        with open(file_path, 'x') as f:
            print(f"File '{file_name}' created inside '{name}'.")
    except FileExistsError:
        print("File already exists.")
        main()

def write_text():
    name = input("Enter directory name where file exists: ")
    file_name = input("Enter file name: ")
    file_path = os.path.join(name, file_name)
    if not os.path.isfile(file_path):
        print("File doesn't exist.")
        main()
    text = input("Enter text to write inside the file (this will overwrite): ")
    try:
        with open(file_path, 'w') as file:
            file.write(text)
        print("Text written successfully.")
    except Exception as e:
        print(f"Error writing to file: {e}")

def read_text():
    name = input("Enter directory name where file exists: ")
    file_name = input("Enter file name: ")
    file_path = os.path.join(name, file_name)
    if not os.path.isfile(file_path):
        print("File doesn't exist.")
        return
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        print("File content:")
        print(content)
    except Exception as e:
        print(f"Error reading file: {e}")

def update_text():
    name = input("Enter directory name where file exists: ")
    file_name = input("Enter file name: ")
    file_path = os.path.join(name, file_name)
    if not os.path.isfile(file_path):
        print("File doesn't exist.")
        return
    text = input("Enter text to append: ")
    try:
        with open(file_path, 'a') as file:
            file.write(text)
        print("Text appended successfully.")
    except Exception as e:
        print(f"Error updating file: {e}")

def get_info():
    name = input("Enter directory name where file exists: ")
    file_name = input("Enter file name: ")
    file_path = os.path.join(name, file_name)
    if not os.path.isfile(file_path):
        print("File doesn't exist.")
        return
    cwd = os.getcwd()
    full_path = os.path.abspath(file_path)
    print(f"Current working directory: {cwd}")
    print(f"Full file path: {full_path}")

def get_name_size():
    name = input("Enter directory name where file exists: ")
    file_name = input("Enter file name: ")
    file_path = os.path.join(name, file_name)
    if not os.path.isfile(file_path):
        print("File doesn't exist.")
        return
    size = os.path.getsize(file_path)
    print(f"File name: {file_name}")
    print(f"File size: {size} bytes")

def get_extension():
    file_name = input("Enter file name (with extension): ")
    _, ext = os.path.splitext(file_name)
    print(f"File extension: '{ext}'")

def delete_file():
    name = input("Enter directory name where file exists: ")
    file_name = input("Enter file name to delete: ")
    file_path = os.path.join(name, file_name)
    if not os.path.isfile(file_path):
        print("File doesn't exist.")
        return
    try:
        os.remove(file_path)
        print("File deleted successfully.")
    except Exception as e:
        print(f"Error deleting file: {e}")

def main():
    while True:    
        print("""
        1. Create a Directory
        2. Create a file
        3. Write
        4. Read
        5. Update
        6. Current Directory and File Path
        7. Name and Size of File
        8. Extention of file
        9. Delete
        0. Exit Program
        """)
        
        choice = int(input("Enter your choice! - "))
        if choice == 1:
            make_dir()
        elif choice == 2:
            make_file()
        elif choice == 3:    
            write_text()
        elif choice == 4:
            read_text()
        elif choice == 5:
            update_text()
        elif choice == 6:
            get_info()
        elif choice == 7:
            get_name_size()
        elif choice == 8:
            get_extension()
        elif choice == 9:
            delete_file()
        elif choice == 0:
            break
        else:
            print("Enter valid choice")

if __name__ == "__main__":
    main()
