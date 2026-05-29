
# Task Tracker CLI 

A simple and efficient Command Line Interface (CLI) application to track your tasks, built with Pure Python without any external dependencies. All data is automatically saved locally in a JSON file.

This project was built as a solution to the [roadmap.sh](https://roadmap.sh/projects/task-tracker) challenge.

##  Features

* **No complex database setup**: Uses a local `tasks.json` file to persist data.
* **Robust error handling**: Validates user inputs (e.g., checks for missing arguments or text where numbers are expected).
* **Auto-incrementing IDs**: Every new task automatically receives a unique identifier.

##  Requirements

* [Python 3.x](https://www.python.org/) installed on your machine. 

##  How to Use

Open your terminal in the folder where `task_tracker.py` is located and run any of the following commands:

### 1. Add a new task
Creates a new task with a default status of `pending`.
```bash
python task_tracker.py add "Buy lactose-free milk"