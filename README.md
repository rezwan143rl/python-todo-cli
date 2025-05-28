📝 To-Do List (Python CLI Project)
A simple command-line to-do list application built using core Python concepts like file handling, loops, and conditionals.  
This project is continuously evolving as I deepen my Python skills!

📌 Features
- Add new tasks with timestamps  
- Delete tasks (completed or incomplete)  
- View all tasks with status and timestamps  
- Mark tasks as completed (with completion time)  
- Persistent storage using a structured JSON file (`tasks.json`)  
- Cross-platform terminal clearing for a clean UI (Windows/macOS/Linux)

🚀 How to Run
Ensure you have Python 3.x installed on your system.

Run the script from your terminal or command prompt:

```bash
python todo.py

Follow the on-screen prompts:
1: Add a new task
2: Delete a task
3: Mark a task as complete
4: View all tasks
5: Exit the app

📂 How It Works
Tasks are saved in tasks.json as objects with properties:

Name: Task description

mark: Completion status (True or False)

time_added: Timestamp when the task was added

time_completed: Timestamp when marked complete (empty if incomplete)

When tasks are added, completed, or deleted, the JSON file updates automatically.
The terminal screen clears after each operation for a neat interface.

📈 Development Roadmap

Initial Version

Basic add, view, and mark completed features with plain text storage.

✨ Update - Functional Version (14.05.2025)

Refactored code into modular functions for better maintainability.

Added prevention of redundant completion marking.

Added delete task feature.

✨ Update - JSON Version (16.05.2025)

Migrated storage to JSON format for structured and scalable data management.

Added timestamps for task creation and completion.

Implemented cross-platform terminal clearing.

✨ Update - Timestamp, Loop, Exit (21.05.2025)

Added cross-platform terminal clearing function (clear_terminal()) for better UI on Windows/macOS/Linux.

Integrated clear_terminal() calls after each user interaction for a cleaner interface.

Improved user experience by adding short delays (time.sleep()) before clearing the terminal.

Refined the main menu loop to handle continuous interaction until exit is chosen.

Overall code cleanup and improved commenting for clarity.

✨ Update - Index Bug Fix and Input Validation (23.05.2025)

Fixed task index misalignment after deletions by reassigning all task indices.

Added input validation for non-integer inputs in menu selection and task indexing.

Improved error handling for smoother user experience.

Optimized allDataStr() output formatting for better readability.

📝 Example JSON Structure
[
  {
    "Index": 1,
    "Name": "Finish homework",
    "mark": false,
    "time_added": "2025-05-21 10:22 PM",
    "time_completed": null
  },
  {
    "Index": 2,
    "Name": "Water the plants",
    "mark": true,
    "time_added": "2025-05-20 09:15 AM",
    "time_completed": "2025-05-21 07:30 PM"
  }
]
👨‍💻 Author
Md. Rezwan Ahmed
Learning Python step by step and sharing my journey through projects!

Feel free to suggest improvements, report issues, or fork the repo.



🤖 Special Thanks

This README and part of the user input validation logic were improved with the help of [ChatGPT by OpenAI](https://openai.com/chatgpt).

- Fixed a bug in the `uinput` part of the code by adding input validation to handle non-integer entries gracefully.
- Helped draft and update this README to clearly reflect the current features and development history.

Learning and improving—one step at a time!
