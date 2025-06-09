def describe_person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")
#calling the function with arbitary keyword arguments

describe_person(name="Rishav", age=24, city="Kathmandu", profession="Student")
