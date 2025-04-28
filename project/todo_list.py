def todo_manager():
    tasks = []
    
    while True:
        print("\nTODO List Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Complete")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            task = input("Enter task: ")
            tasks.append({"task": task, "completed": False})
            print("Task added!")
            
        elif choice == "2":
            if not tasks:
                print("No tasks yet!")
            else:
                for i, task in enumerate(tasks, 1):
                    status = "✓" if task["completed"] else " "
                    print(f"{i}. [{status}] {task['task']}")
                    
        elif choice == "3":
            task_num = int(input("Enter task number to mark complete: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num-1]["completed"] = True
                print("Task marked complete!")
            else:
                print("Invalid task number")
                
        elif choice == "4":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice")

if __name__ == "__main__":
    todo_manager()
