import time

user_input = int(input("Enter the current time: "))

if user_input >= 9:
    print("It is still morning.")
elif user_input >= 12:
    print("It is after noon.")
elif user_input >= 18:
    print("It is evening.")
else:
    print("It is night time.")
