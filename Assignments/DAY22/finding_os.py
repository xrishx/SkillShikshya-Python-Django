# WHICH OS IS IT Using import OS
import os

ops = os.name
if ops == "nt":
    print("You are using Windows!")
elif ops == "posix":
    print("You are using MacOS or Linux!")