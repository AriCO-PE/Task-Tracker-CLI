import json
from sys import argv

#error validation
if len(argv) < 2:
    print("Usage: python task_tracker.py <task_file.json>")
    exit(1)

#user control
command = argv[1]
file = "tasks.json"


#command add

if command == "add":
    if len(argv) < 3:
        print("error: missing task description for 'add' command")
        exit(1)
    else:
        task_name   = argv[2]

    try:
        with open(file, "r") as f:
            tasks = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []


# calculate ID
    new_id = tasks[-1]["id"] + 1 if tasks else 1


#JSON
    new_task = {"id": new_id,
                "name": task_name,
                "status": "pending"}
    tasks.append(new_task)

    with open(file, "w") as f:
        json.dump(tasks, f, indent=4)
    print(f"Task '{task_name}' added successfully (ID: {new_id}).")


# command list
elif command == "list":
    try:
        with open(file, "r") as f:
            tasks = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
       
    
    if not tasks:
        print("No tasks found.")
    else:
        print("\n/--- Tasks ---/")
        for task in tasks:
            print(f"ID: {task['id']} | Name: {task['name']} | Status: {task['status']}")
        print("/-------------/\n")



# command delete 

elif command == "delete":
    if len(argv) < 3:
        print("error: missing task ID for 'delete' command")
        exit(1)
    else:
        try:
            task_id = int(argv[2])
        except ValueError:
            print("error: task ID must be an integer")
            exit(1)

    try:
        with open(file, "r") as f:
            tasks = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []

    # function delete
    tasks = [t for t in tasks if t["id"] != task_id]

    
    #save
    with open(file, "w") as f:
        json.dump(tasks, f, indent=4)
    print(f"Task with ID {task_id} deleted successfully.")

#update
elif command == "update-":
    if len(argv) < 4:
        print("error: missing task ID or new status for 'update' command")
        exit(1)
    else: 
        try:
            task_id = int(argv[2])
        except ValueError:
            print("error: task ID must be an integer")
            exit(1)
        new_name = argv[3]
    
    try: 
        with open(file, "r") as f:
            tasks = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
    