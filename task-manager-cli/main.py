def load_tasks(filename):
    """Load tasks from file and return a list of task dicts."""
    tasks = []

    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()

                if line == "":
                    continue

                parts = line.split("|")

                task = {
                    "id": parts[0].strip(),
                    "status": parts[1].strip(),
                    "desc": parts[2].strip()
                }

                tasks.append(task)

    except FileNotFoundError:
        return []

    return tasks


def save_tasks(filename, tasks):
    """Save the tasks list to file."""
    with open(filename, "w", encoding="utf-8") as f:
        for task in tasks:
            line = f"{task['id']} | {task['status']} | {task['desc']}\n"
            f.write(line)


def add_task(filename, description):
    """Add a new task with PENDING status."""
    tasks = load_tasks(filename)

    if tasks:
        new_id = int(tasks[-1]["id"]) + 1
    else:
        new_id = 1

    tasks.append({
        "id": new_id,
        "status": "PENDING",
        "desc": description
    })
    save_tasks(filename, tasks)
    return


def complete_task(filename, task_id):
    """Mark a task as DONE by its ID."""
    tasks = load_tasks(filename)
    for task in tasks:
        if int(task["id"]) == task_id:
            task["status"] = "DONE"
    save_tasks(filename, tasks)
    return


complete_task("tasks.txt", "2")


def list_tasks(filename):
    """Display all tasks with their status."""
    list_tasks = []
    done = ["✅"]
    pending = []
    tasks = load_tasks(filename)
    for task in tasks:
        list_task = list(task.values())
        if task["status"] == "DONE":
            list_task.append(done)
        elif task["status"] == "PENDING":
            list_task.append(pending)
        list_tasks.append(list_task)
    print(list_tasks)


def main():
    """Run the interactive task manager CLI."""
    FILENAME = "tasks.txt"

    while True:
        print("\n=== To-Do List Manager ===")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Mark task as completed")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
             list_tasks(FILENAME)

        elif choice == "2":
            desc = input("Task description: ")
            add_task(FILENAME, desc)
            print("Task added successfully!")

        elif choice == "3":
            task_id = int(input("Task number: "))
            complete_task(FILENAME, task_id)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
