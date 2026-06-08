def display_tasks(task_list):
    """Displays the list of tasks."""
    print("\nCurrent To-Do List:")
    for i, task in enumerate(task_list, start=1):
        print(f"{i}.{task}")

def filter_tasks(task_list, keyword):
    """Placeholder for filtering tasks (students will implement)."""
    filtered = [task for task in task_list if keyword.lower() in task.lower()]
    print(f"\nTasks containing '{keyword}':")
    display_tasks(filtered)

def task_generator(task_list, keyword):
    return (task for task in task_list if keyword.lower() in task.lower())