print("Welcome to to-do-py")
username = input("Enter your username : ")
with open('./to-do-py-usernames.txt', 'r+') as userfile:
    users = userfile.readline()
    if username not in users:
        print(f"Hi, {username}!")
        userfile.write(username)
    else:
        print(f"Welcome back, {username}")
user_choice = input(
    "To add new task enter 'a' ,to open your tasks enter 'o' or to quit enter 'q' : ")
while user_choice == 'a' or user_choice == 'o':
    if user_choice == 'a':
        with open('./to-do-tasks.txt', 'a') as to_do_task_file:
            task = input("Enter the task : ")
            to_do_task_file.write(f"{task}\n")
    elif user_choice == 'o':
        with open('./to-do-tasks.txt', 'r') as to_do_task_file:
            to_do_tasks = to_do_task_file.readlines()
            index_of_task = 1
            for line in to_do_tasks:
                print(f"{index_of_task}. {line.strip()}")
                index_of_task += 1
    user_choice = input(
        "To add new task enter 'a' ,to open your tasks enter 'o' or to quit enter 'q' : ")
