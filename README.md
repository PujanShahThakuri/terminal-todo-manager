 📝 Terminal-Based To-Do List App (Python)

This is a simple and user-friendly **To-Do List application** built with Python that runs in the terminal. It helps you manage your daily tasks by allowing you to add, view, mark as done/undone, delete, and organize tasks with due dates, priorities, and categories.

---

## 🚀 Features

- ✅ Add tasks with:
  - Description
  - Optional due date (`YYYY-MM-DD`)
  - Priority (High, Medium, Low)
  - Category (e.g., Work, Personal)
- 📋 View all tasks sorted by priority and due date
- 🔁 Mark tasks as **done/undone**
- ❌ Delete tasks
- 💾 Saves your tasks in a `tasks.txt` file so nothing is lost
- 📂 Auto-sorts tasks: High priority and earliest due dates come first

---

## 🧠 How It Works

- Tasks are stored in `tasks.txt` in the format:
[x] Do homework ##2025-06-28 ##High ##School
[ ] Buy groceries ##2025-06-30 ##Medium ##Home

css
Copy
Edit

- Internally, each task is a dictionary:
```python
{
  "done": False,
  "desc": "Buy groceries",
  "due": "2025-06-30",
  "priority": "Medium",
  "category": "Home"
}
Tasks are automatically sorted by priority (High > Medium > Low), and then by due date.

🛠️ How to Run
Make sure you have Python installed.

Save the script as to-do-list.py.

Open a terminal and run:

bash
Copy
Edit
python to-do-list.py
📂 Files
to-do-list.py: Main Python script

tasks.txt: Stores your tasks (auto-generated)

📌 Example Menu
markdown
Copy
Edit
Menu:
1. View tasks
2. Add task
3. Mark task done/undone
4. Delete task
5. Exit
🔐 Requirements
Python 3.x

No external libraries — only built-in modules (os, datetime)

📈 Future Ideas
Reminders with notifications

Recurring tasks

Color-coded terminal output

GUI version (Tkinter or web app)

🙌 Author
Made by Pujan Shahi Thakuri
Simple. Clean. Just works.

🧾 License
This project is open-source and free to use
