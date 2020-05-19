# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2020,Created started script
# Jeff Nelson,2020-05-17, Major updates for assignment 5
# Jeff Nelson,2020-05-18, Updated file initial file handling
# ------------------------------------------------------------------------ #

# Import libaray
import os

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
strTask = "" # Captures user task input
strPriority = "" # Captures user priority

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here

# Change the absolute path of the python file location
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Checks to see if there is in the same directory as the python file. If not it creates a blank file.
if os.path.exists("ToDoList.txt"):
    objFile = open(objFile, "r")
    for row in objFile:
        t, p = row.split(",")
        # print(t, p)
        dicRow = {"Task": t, "Priority": p.strip()}
        lstTable.append(dicRow)
        # print(lstTable)
    objFile.close()
else:
    objFile = open(objFile, "w")
    objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current task list.
    2) Add a new task and priority.
    3) Remove an existing task.
    4) Save Data to ToDoList.txt
    5) Exit Program.
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        i = 0
        for row in lstTable:
            print('  ', row['Task'], ', ', row['Priority'], sep='')
            i = 1
        if (i == 0):
            print("No tasks in file. Ready to add tasks!")
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        while (True):
            strTask = input("What is the task: ")
            strPriority = input("What is the priority: ")
            # Clean up user inputs
            strTask = strTask.strip()
            strPriority = strPriority.strip()
            # Append inputs to the list
            lstTable.append({"Task": strTask.title(), "Priority": strPriority.title()})
            strChoice = input("Add another task: ('y/n'): ")
            if strChoice.lower() == 'n':
                # print(lstTable)
                break
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        while (True):
            strTask = input("Task to remove: ")
            for row in lstTable:
                if row['Task'].lower() == strTask.lower():
                    lstTable.remove(row)
                    print("Task removed from list")
                else:
                    print("Task not found")
            strChoice = input("Remove another task? ('y/n'): ")
            if strChoice.lower() == 'n':
                break
        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        objFile = open("ToDoList.txt", "w")
        for row in lstTable:
            objFile.write(str(row["Task"]) + ", " + str(row["Priority"]) + "\n")
        objFile.close()
        print("Tasks saved to ToDoList.txt")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        break  # and Exit the program
    else:
        print(" Only 1,2,3,4 or 5 are valid inputs. Please choose one.")
