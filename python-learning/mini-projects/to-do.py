tasks = []
while True:
    print("\n----- To-Do List Menu -----")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")
    choice = input("Choose")
    
    if choice == "1":
        
        task = input("Enter your new task: ")
        tasks.append(task)
        print("Task added. ")
    elif choice == "2":
        
        print("\nYour Tasks:")
        if len(tasks) == 0:
            print("No tasks yet!")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {tasks}")
    elif choice == "3":
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print("{i}. {task}") 
        task_num = input("Enter the number of the task to remove")       
        if task_num.isdigit():
            task_num = int(task_num)
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"removed: {removed}")
            else:
                print("Invalid task number.")
        else:
            print("Please enter a valid number.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choost 1-4.")