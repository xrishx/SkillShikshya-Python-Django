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

    weekday_count = 0
    current_date = today_date

    while weekday_count < no_students:
        weekday = current_date.weekday()

        if weekday < 5:
            print(f"{students[weekday_count]} for {current_date}.")
            weekday_count += 1
        else:
            print(f"No presentaion on {current_date} and {current_date+datetime.timedelta(days=1)} as it's weekend.")
        current_date += datetime.timedelta(days=1)

        if weekday >= 5:
            while current_date.weekday() >= 5:
                current_date += datetime.timedelta(days=1)

add_user()




