import os
import json
from prettytable import PrettyTable
from colorama import Fore, Style, init
import sys

init(autoreset=True)  # Initialize colorama

password = open('user.txt', 'r').read() #change if you want

# Load existing data from the JSON file
with open('todos.json', 'r') as todos:
    todos_data = json.load(todos)

def display_todos(todos_dict):
    table = PrettyTable()
    table.field_names = ["Todo Name", "Description", "Status"]
    table.border = True  # Add borders
    
    for todo_name, todo_info in todos_dict.items():
        name_colored = f"{Fore.WHITE}{todo_name}{Style.RESET_ALL}"
        desc_colored = f"{Fore.WHITE}{todo_info['todo_description']}{Style.RESET_ALL}"
        if todo_info['status'] == "Completed":
            status_colored = f"{Fore.GREEN}{todo_info['status']}{Style.RESET_ALL}"
        elif todo_info['status'] == "Incomplete":
            status_colored = f"{Fore.RED}{todo_info['status']}{Style.RESET_ALL}"
        table.add_row([name_colored, desc_colored, status_colored])
    
        # Add a separator row made of dashes (-) between rows
        table.add_row([" " * len(name_colored), " " * len(desc_colored), " " * len(status_colored)])
    
    # Print the table with borders and separators
    print(table)



def update_todo_status(todo_name, new_status):
    try:
        if todo_name in todos_data['Todos']:
            todos_data['Todos'][todo_name]['status'] = new_status
            with open('todos.json', 'w') as file:
                json.dump(todos_data, file, indent=4)
            print(f"Todo '{todo_name}' status updated to '{new_status}'!")
        else:
            print(f"Todo '{todo_name}' does not exist.")
    except KeyError:
        print(f"Todo '{todo_name}' does not exist.")

def help():
    print("Welcome to your terminal-based todo Manager.")
    print(f"{Fore.CYAN}Available commands:")
    print(f"{Fore.YELLOW}- add todo <todo_name>: Add a new todo")
    print(f"{Fore.YELLOW}- del todo <todo_name>: Delete a todo")
    print(f"{Fore.YELLOW}- list todos: List all todos")
    print(f"{Fore.YELLOW}- complete todo <todo_name>: Mark a todo as completed")
    print(f"{Fore.YELLOW}- clear: Clear the screen")
    print(f"{Fore.YELLOW}- help: Display this help message")
    print(f"{Fore.YELLOW}- change password: change the password")
    print(f"{Fore.YELLOW}- del all todos: Delete all your todos")
    print(f"{Fore.YELLOW}- exit: Exit the program{Style.RESET_ALL}")
    print("\n\n")

def dashboard():
    while True:
        command = input("What do you want to do : ")

        if "add todo" in command:
            extract_todo_name = command.split(" ")
            todo_name = extract_todo_name[-1]
            todo_description = input("Todo Description : ")
            todo_status = "Incomplete"

            todos_data["Todos"][todo_name] = {
                "todo_description": todo_description,
                "status": todo_status
            }
            with open('todos.json', 'w') as file:
                json.dump(todos_data, file, indent=4)
            print(f"Todo '{todo_name}' added successfully!")
            display_todos(todos_data["Todos"])
        elif "del todo" in command:
            extract_todo_name2 = command.split(" ")
            todo_name2 = extract_todo_name2[-1]
            if todo_name2 in todos_data['Todos']:
                del todos_data["Todos"][todo_name2]
                with open('todos.json', 'w') as file:
                    json.dump(todos_data, file, indent=4)
                print(f"Todo '{todo_name2}' deleted successfully!")
                display_todos(todos_data["Todos"])
            else:
                print(f"Todo '{todo_name2}' not found.")
        elif command == "list todos":
            display_todos(todos_data["Todos"])
        elif "complete todo" in command:
            extract_todo_name3 = command.split(" ")
            todo_name3 = extract_todo_name3[-1]
            update_todo_status(todo_name3, "Completed")
            display_todos(todos_data["Todos"])
        elif command == "clear":
        	os.system('clear')
        elif command == "help":
        	help()
        elif command == "exit":
        	print("Exiting the program...")
        	sys.exit()
        elif command == "change password":
        	new_password = input("Enter new password : ")
        	update = open('user.txt', 'w')
        	update.write(new_password)
        	update.close()
        elif command == "del all todos":
            todos_data["Todos"].clear()
            print("All todos are deleted")
            with open('todos.json', 'w') as file:
                json.dump(todos_data, file, indent=4)
def auth(password_auth):
    if password_auth == password:
        help()
        dashboard()
    else:
        print("Incorrect Password")

auth(input("Enter your password: "))
