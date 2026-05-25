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
