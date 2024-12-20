import pytest
from datetime import datetime
from my_habits import MyHabits
from analytics_module import display_analytics_summary, get_longest_streak_for_habit
from db_manager import create_connection, create_tables


@pytest.fixture(scope='module')
def test_db():
    # Create a test database connection
    dbconnection = create_connection()
    dbcursor = dbconnection.cursor()

    # Set SQLite to handle database access more leniently
    dbcursor.execute('PRAGMA journal_mode=WAL;')  # Write-Ahead Logging can reduce locking issues
    dbcursor.execute('PRAGMA synchronous=NORMAL;')  # Reduce synchronization overhead

    # Create the necessary tables
    create_tables(dbcursor)

    # Get the current date
    current_date = datetime.now().date().strftime("%Y-%m-%d")

    # Insert initial data
    dbcursor.execute("""INSERT INTO Habits (habit_name, habit_period, creation_date, last_completed, streak, habit_status) SELECT ?, ?, ?, ?, ?, ? 
    WHERE NOT EXISTS (SELECT 1 FROM Habits WHERE habit_name = ? AND habit_period = ?)""", 
    ("Cycling", "daily", current_date, None, 0, 'active', "Cycling", "daily"))

    dbcursor.execute("""INSERT INTO Habits (habit_name, habit_period, creation_date, last_completed, streak, habit_status) SELECT ?, ?, ?, ?, ?, ? 
    WHERE NOT EXISTS (SELECT 1 FROM Habits WHERE habit_name = ? AND habit_period = ?)""", 
    ("Hiking", "weekly", current_date, None, 0, 'active', "Hiking", "weekly"))

    dbconnection.commit()
    
    # Provide the connection to the tests
    yield dbconnection
    
    # Teardown
    dbconnection.close()

@pytest.fixture
def my_habits(test_db):
    return MyHabits(test_db)

def test_add_habit(my_habits, test_db):
    habit_name = "Read Books"
    habit_period = 1

    my_habits.add_habit(habit_name, habit_period)

    dbcursor = test_db.cursor()
    dbcursor.execute("SELECT * FROM Habits WHERE habit_name = ?", (habit_name,))
    dbcursor.fetchone()

def test_remove_habit(my_habits, test_db):
    dbcursor = test_db.cursor()
    dbcursor.execute("SELECT id FROM Habits WHERE habit_name = ? AND habit_status = 'active'", ("Read Books",))
    habit_id = dbcursor.fetchone()[0]

    my_habits.remove_habit(habit_id)

    dbcursor.execute("SELECT * FROM Habits WHERE id = ?", (habit_id,))
    dbcursor.fetchone()

def test_list_all_habits(my_habits):
    my_habits.list_all_habits()

def test_check_off_task(my_habits, test_db):
    dbcursor = test_db.cursor()

    dbcursor.execute("SELECT id FROM Habits WHERE habit_name = ?", ("Cycling",))
    cycling_habit_id = dbcursor.fetchone()[0]
    print(cycling_habit_id)

    my_habits.check_off_task(cycling_habit_id)

    dbcursor.execute("SELECT * FROM Tasks WHERE habit_id = ?", (cycling_habit_id,))
    dbcursor.fetchone()

    dbcursor.execute("SELECT id FROM Habits WHERE habit_name = ?", ("Hiking",))
    hiking_habit_id = dbcursor.fetchone()[0]

    my_habits.check_off_task(hiking_habit_id)
    
    dbcursor.execute("SELECT * FROM Tasks WHERE habit_id = ?", (hiking_habit_id,))
    dbcursor.fetchone()


def test_get_completed_tasks(my_habits):
    my_habits.get_completed_tasks()

def test_list_all_tasks(my_habits):
    my_habits.list_all_tasks()


def test_display_analytics_summary():
    # Check the analytics summary for habits
    display_analytics_summary()


def test_get_longest_streak_for_habit(test_db):
    dbcursor = test_db.cursor()
    dbcursor.execute("SELECT id FROM Habits WHERE habit_name = ?", ("Cycling",))
    habit_name = dbcursor.fetchone()[0]

    get_longest_streak_for_habit(habit_name)


