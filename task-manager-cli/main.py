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
