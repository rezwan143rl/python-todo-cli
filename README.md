# 📝 To-Do List (Python CLI Project)

A simple command-line to-do list application built using basic Python concepts like file handling, loops, and conditionals. This is my first project after learning core Python — it will be updated as I learn more!

---

## 📌 Features

- Add a new task
- delete a task (updated)
- View all tasks
- Mark tasks as completed

---

## 🚀 How to Run

1. Make sure you have Python installed (Python 3.x).
2. Run the script:


python todo.py
Follow the prompts:

Type 1 to add a task

Type 2 to mark a task as completed

Type 3 to view all tasks

📂 How It Works
Tasks are stored in a plain text file named tasks.txt

When you add or update a task, the file is modified directly

Completed tasks get a (completed) tag

📈 What's Next
This is a beginner version. I'm planning to:

 Add a delete task option (checked)(14.05.2025)

 Improve user interface

 Switch to OOP structure

 Use JSON for better data storage

 Add task numbering for easier use

 Build a GUI or web version in the future

                       ✨ Update - Functional Version(14.05.2025)

The code has been refactored into a modular structure using functions, which makes it more maintainable and readable.

✅ Features Added:
add() function: Appends new tasks to the file.

allDataStr() function: Reads and returns all tasks.

mark_completed() function: Marks a task as complete and prevents duplicate completion.

Prevents redundant marking of tasks already marked as completed.

Cleaner main menu with function calls.

#####Delete Task Feature#####

You can now delete a task by selecting option 2.

The app checks both completed and incomplete versions of the task and removes it.

Example flow:
choose:
1.Add task
2.Delete task
3.Mark task as complete
4.view all task
                                  ✨ Update - JSON Version(16.05.2025)
## 📝 To-Do CLI App (JSON Version)

This updated version of the CLI to-do list app now uses structured JSON storage instead of plain text. Each task is saved as an object with a name and completion status.

### Features
- ✅ Add a new task
- ✅ Delete a task
- ✅ Mark a task as completed
- ✅ View all tasks with their status
- ✅ JSON file (`tasks.json`) for persistent, structured storage

### Example JSON Task Format
```json
[
  {
    "Name": "Finish homework",
    "mark": false
  },
  {
    "Name": "Water the plants",
    "mark": true
  }
]
👨‍💻 Author
Made by Md. Rezwan Ahmed while learning Python!
Feel free to suggest improvements or fork the project.

