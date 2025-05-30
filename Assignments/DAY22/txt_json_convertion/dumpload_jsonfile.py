import json

def txt_json():
    try:    
        with open("Assignments/DAY22/txt_json_convertion/txt_file.txt", "r") as file:
            content = file.read()
            json_data = json.loads(content)
        with open("Assignments/DAY22/txt_json_convertion/json_file.json", "w") as file:
            json.dump(json_data, file, indent = 4)
        print("Converted to .json successfully")
        print("Converted .json data:\n", json.dumps(json_data, indent=4))
    except json.JSONDecodeError:
        print("Error: The TXT file does not contain valid JSON.")
    except FileNotFoundError:
        print("Error: txt_file.txt not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")

def json_txt():
    try:
        with open("Assignments/DAY22/txt_json_convertion/json_file.json", "r") as file:
            json_data = json.load(file)
        with open("Assignments/DAY22/txt_json_convertion/txt_file.txt", "w") as file:
            data = json.dumps(json_data, indent=4)
            file.write(data)
        print("Converted to .txt successfully")
        print("Converted .txt data:\n", json.dumps(json_data, indent=4))     
    except json.JSONDecodeError:
        print("Error: The JSON file contains invalid data.")
    except FileNotFoundError:
        print("Error: json_file.json not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")


print("""
    1. .txt to .json
    2. .json to .txt
    """)
choice = input("What would you like to do?> ")
if choice == "1":
    txt_json()
elif choice == "2":
    json_txt()
else:
    print("Enter valid choice!")