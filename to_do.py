import os.path

print("🙇 Welcome to to-do-py,\n")
userName = input("What is your name ?\n> ")
if(os.path.isfile('./tdp_username.txt')):
    with open('./tdp_username.txt', 'a+') as userfile:
        users = userfile.readline()
        if userName not in users:
            print(f"Hello 👋, {userName}!")
            userfile.write(f"{userName}")
        else:
            print(f"Hello 👋, {userName}! Nice to see you again,")
else:
    with open('./tdp_username.txt', 'w+') as userfile:
        users = userfile.readline()
        if userName not in users:
            print(f"Hello 👋, {userName}!")
            userfile.write(f"{userName}")
        else:
            print(f"Hello 👋, {userName}! Nice to see you again,")

print("\n🔢 Options :\n1. Press 🇦  to add new task.\n2. Press 🇴  to display tasks.\n3. Press 🇶  to quit.\n\n")
userChoice = input("So what do you want to do ? 👇,\n> ").lower()

while userChoice == 'a' or userChoice == 'o':
    if userChoice == 'a':
        if(os.path.isfile('./tdp_tasks.txt')):
            with open('./tdp_tasks.txt', 'a') as tdpFile:
                task = input("Enter the task 👇,\n> ")
                tdpFile.write(f"{task}\n")
        else:
            with open('./tdp_tasks.txt', 'w') as tdpFile:
                task = input("Enter the task 👇,\n> ")
                tdpFile.write(f"{task}\n")
    elif userChoice == 'o':
        with open('./tdp_tasks.txt', 'r') as tdpFile:
            tdp_tasks = tdpFile.readlines()
            numberOfTasks = 1
            for line in tdp_tasks:
                print(f"{numberOfTasks}. {line.strip()}")
                numberOfTasks += 1
    print("\n🔢 Options :\n1. Press 🇦  to add new task.\n2. Press 🇴  to display tasks.\n3. Press 🇶  to quit.\n\n")
    userChoice = input("So what do you want to do ? 👇,\n> ")
