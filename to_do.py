print("š Welcome to to-do-py,\n")
userName = input("What is your name ?\n> ")
with open('./tdp_username.txt', 'a+') as userfile:
    users = userfile.readline()
    print(f"Hello š, {userName}!")
    userfile.write(f"{userName}")

print("\nš¢ Options :\n1. Press š¦  to add new task.\n2. Press š“  to display tasks.\n3. Press š¶  to quit.\n\n")
userChoice = input("So what do you want to do ? š,\n> ").lower()

while userChoice == 'a' or userChoice == 'o':
    if userChoice == 'a':
        with open('./tdp_tasks.txt', 'a+') as tdpFile:
            task = input("Enter the task š,\n> ")
            tdpFile.write(f"{task}\n")
    elif userChoice == 'o':
        with open('./tdp_tasks.txt', 'r') as tdpFile:
            tdp_tasks = tdpFile.readlines()
            numberOfTasks = 1
            for line in tdp_tasks:
                print(f"{numberOfTasks}. {line.strip()}")
                numberOfTasks += 1
    print("\nš¢ Options :\n1. Press š¦  to add new task.\n2. Press š“  to display tasks.\n3. Press š¶  to quit.\n\n")
    userChoice = input("So what do you want to do ? š,\n> ")
