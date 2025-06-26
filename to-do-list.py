import os
import datetime

TASKS_FILE = "tasks.txt"

def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE) as f:
            for line in f:
                line = line.strip()
                if not line: continue
                done = line[1] == "x"
                content = line[4:]
                # Now split by ## expecting desc ## due ## priority ## category
                parts = content.split("##")
                desc = parts[0].strip()
                due = parts[1].strip() if len(parts) > 1 else ""
                priority = parts[2].strip() if len(parts) > 2 else "Medium"
                category = parts[3].strip() if len(parts) > 3 else "General"
                tasks.append({"done": done, "desc": desc, "due": due,
                              "priority": priority, "category": category})
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        for t in tasks:
            status = "x" if t["done"] else " "
            f.write(f"[{status}] {t['desc']} ##{t['due']} ##{t['priority']} ##{t['category']}\n")
    print("✔️ Tasks saved.")

def valid_date(date_str):
    if not date_str:
        return True
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def sort_tasks(tasks):
    def priority_value(p):
        return {"High": 1, "Medium": 2, "Low": 3}.get(p, 2)
    def key(t):
        try:
            due_date = datetime.datetime.strptime(t["due"], "%Y-%m-%d")
        except:
            due_date = datetime.datetime.max
        return (priority_value(t["priority"]), due_date)
    tasks.sort(key=key)

def show_tasks(tasks):
    if not tasks:
        print("You have no tasks.")
        return
    sort_tasks(tasks)
    print("\nYour tasks:")
    for i, t in enumerate(tasks, 1):
        status = "✓" if t["done"] else " "
        due = f" (Due: {t['due']})" if t["due"] else ""
        print(f"{i}. [{status}] {t['desc']}{due} [Priority: {t['priority']}, Category: {t['category']}]")

def add_task(tasks):
    desc = input("Task description: ").strip()
    if not desc:
        print("Task cannot be empty.")
        return

    due = input("Due date (YYYY-MM-DD) or leave blank: ").strip()
    while not valid_date(due):
        due = input("Invalid date. Enter again or leave blank: ").strip()

    priority = input("Priority (High, Medium, Low) [Medium]: ").strip().capitalize()
    if priority not in ("High", "Medium", "Low"):
        priority = "Medium"

    category = input("Category [General]: ").strip()
    if not category:
        category = "General"

    tasks.append({"done": False, "desc": desc, "due": due,
                  "priority": priority, "category": category})
    save_tasks(tasks)
    print(f"Added task: {desc}")

def toggle_done(tasks):
    if not tasks:
        print("No tasks available.")
        return
    try:
        n = int(input("Enter task number to mark done/undone: "))
        if 1 <= n <= len(tasks):
            tasks[n-1]["done"] = not tasks[n-1]["done"]
            save_tasks(tasks)
            print(f"Task '{tasks[n-1]['desc']}' marked {'done' if tasks[n-1]['done'] else 'not done'}.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    if not tasks:
        print("No tasks available.")
        return
    try:
        n = int(input("Enter task number to delete: "))
        if 1 <= n <= len(tasks):
            removed = tasks.pop(n-1)
            save_tasks(tasks)
            print(f"Deleted task: {removed['desc']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("""
Menu:
1. View tasks
2. Add task
3. Mark task done/undone
4. Delete task
5. Exit
""")
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            toggle_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()
