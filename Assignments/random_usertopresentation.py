# https://stackoverflow.com/questions/26124531/getting-the-date-for-next-weekday

import datetime
import random

# List of students
students = ["Rishav", "Tenzi", "Novel"]
today_date = datetime.date.today()      # Get today Date

# Asking if you wanna add more user to list 
def add_user():
    add = input("Do you want to add more User? (y/n): ")

    if add.lower() == "y":
        new_user = input("Enter the name of User: ")
        students.append(new_user)
        no_students = len(students)
        return add_user()
    elif add.lower() == "n":
        no_students = len(students)
        return coming_weekdays(no_students)
    else:
        print("Enter valid response")
        return add_user()

def coming_weekdays(no_students):
    random.shuffle(students)
    print(students)
    for x in range(0, no_students):
        # timedelta to add to today date
        total_dates = today_date + datetime.timedelta(days=x)
        weekday = total_dates.weekday()
        # Getting weekdays (0 - 6, Mon - Sun)
        if weekday < 5:
            print(f"{students[x]} for {total_dates}")
        else:
            no_students += 1
            print(f"No presentation on {total_dates} as weekend.") 
            


add_user()




