# **Habit-Tracker Application**

A habit tracking app written in Python that allows users to create, manage, and track daily or weekly habits.

---

### **Tools Used**:

- **Python**: The primary language used to build the app.
- **SQLite3**: The database used to store habit and task information locally on the user's machine.
- **pytest**: A testing framework used for unit testing the application.

---

### **Installation Guide**:

1. **Download and Save Files**:

   - Clone the repository on your machine.

2. **Navigate to the Folder**:

   - Open your **command line/terminal** and navigate to the folder where you saved the files using the `cd` command:
     ```bash
     cd /path/to/your/folder
     ```

3. **Run the Application**:

   - Start the application by running the following command:
     ```bash
     python habits.py
     ```
   - Ensure that **Python 3.7 or later** is installed on your machine.

4. **Testing with `pytest`**:

   - The application uses **pytest** for unit testing. To run the tests, you will need to have **pytest** installed.

     - You can install pytest by running the following command:
       ```bash
       pip install pytest
       ```

   - To start the tests, run this command:
     ```bash
     pytest test.py
     ```
   - **Test File Example**:
     - The tests for this application are in a Python file that imports the app’s modules, like `my_habits.py` and `analytics_module.py`, and test functionality such as adding, removing, and listing habits. It uses fixtures to set up and tear down the database, as well as assertions to validate expected behavior.

---

### **How to Use the Application**:

Once the application starts, the user is presented with a **menu** displayed on the command line interface. The menu contains a list of actions you can perform, each associated with a unique number. To select an action, simply type the corresponding number and press **Enter**.

---

### **App Menu Options**:

- **ENTER 1**: Create/Add a new habit.

  - **Function**: This option allows you to create a new habit by specifying its name and whether it's a daily or weekly habit.
  - **Process**: After selecting this option, you will be prompted to:
    - Enter the habit's name.
    - Specify whether it’s a **daily** or **weekly** habit by entering `1` for daily or `2` for weekly.

- **ENTER 2**: Remove an existing habit.

  - **Function**: This option lists your active habits and allows you to remove one by entering its ID.
  - **Process**: You will be shown a list of your current habits along with their IDs. Enter the ID of the habit you want to remove.

- **ENTER 3**: List all existing habits.

  - **Function**: This option displays all your active habits, showing their names, periodicity (daily/weekly), and current streaks.
  - **Process**: The list of active habits is printed on the terminal.

- **ENTER 4**: List habits by periodicity.

  - **Function**: This option allows you to filter your habits based on their periodicity (daily or weekly).
  - **Process**: After selecting this option, you will be prompted to enter `1` for daily habits or `2` for weekly habits, and the relevant habits will be displayed.

- **ENTER 5**: Log/Check off a completed habit task.

  - **Function**: This option lets you log a habit task as completed, and the app will automatically update your streak.
  - **Process**: After selecting this option, you will be prompted to:
    - Enter the habit ID that you have completed.
    - The system will update the streak and mark the task as completed.

- **ENTER 6**: View tasks completed today.

  - **Function**: This option displays all tasks that have been completed today.
  - **Process**: The tasks are retrieved from the database and printed on the terminal, along with the habit names and timestamps.

- **ENTER 7**: View all tasks.

  - **Function**: This option displays all tasks in the database.
  - **Process**: The tasks are retrieved from the database and printed on the terminal, along with the habit names and timestamps.

- **ENTER 8**: analyze user habit.

  - **Function**: This option analyzes user habit in the database.
  - **Process**: The `analyze_user_habits` function retrieves and summarizes key insights from the database on user habit patterns, highlighting streaks, current habits, and areas needing improvement.

- **ENTER 9**: Get longest streak for a specific habit.

  - **Function**: This option returns longest streak for a specific habit in the database.
  - **Process**: This function retrieves longest streak of a specific habit from the database.

- **ENTER 0**: Exit the application.

---

### **Additional Features**:

- **Streak Management**: The app tracks habit streaks, meaning it records how many consecutive days or weeks you’ve completed a habit. If you complete a task on consecutive days, your streak will increase automatically.

- **Data Persistence**: All habit and task data is stored in an SQLite3 database. This ensures that your data is saved even after closing the application, and you can resume from where you left off when you restart the app.

---

### **Error Handling and Input Validation**:

- The app includes basic error handling to ensure smooth user experience. For example, if you enter an invalid habit ID when trying to remove or log a habit, the app will display an appropriate error message.
- It also validates your inputs (e.g., ensuring you select either `1` or `2` for daily/weekly habits).

---

### **Known Limitations**:

- Currently, the app only supports simple habit tracking for daily and weekly habits. Future updates could include additional features like notifications, more detailed analytics, and reminders.

---

### **Troubleshooting**:

- **If the app does not start**:
  - Ensure you have Python 3.7 or later installed on your machine.
  - Check that the SQLite3 database file is located in the same folder as the `habits.py` file.
  - If Python is not recognized, ensure Python is added to your system’s PATH or try running the command `python3 habits.py` instead of `python habits.py`.
