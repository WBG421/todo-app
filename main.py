import time
from helpers import open_todos, save_todos


def main():
    t = time.strftime("%d %b %Y %H:%M:%S", time.localtime())
    print("It is " + t)
    print("Anything")
    while True:
        user_prompt = "You can add, complete, show, edit, wipe and exit: "
        user_action = input(user_prompt)
        if user_action.startswith("add"):
            todo = input("Enter a todo: ")
            todos = open_todos()
            todos.append(todo)
            save_todos(todos)
        elif user_action.startswith("complete"):
            todos = open_todos()
            while True:
                try:
                    number = input("Which todo you want to complete? ")
                    number = int(number)
                    if not 0 < number <= len(todos):
                        raise ValueError
                    break
                except ValueError:
                    print(f"Please enter a valid integer in range of the todo list.")
                    pass
            removed_todo = todos[number - 1]
            todos.pop(number - 1)
            save_todos(todos)
            print(f"Removed {removed_todo} from the todos.")
        elif user_action.startswith("show"):
            todos = open_todos()
            for i, todo in enumerate(todos):
                print(f"{i + 1}.{todo}")
        elif user_action.startswith("edit"):
            todos = open_todos()
            while True:
                try:
                    number = input("Which todo you want to edit? ")
                    number = int(number)
                    if not 0 < number <= len(todos):
                        raise ValueError
                    break
                except ValueError:
                    print("Please enter a valid integer in range of the todo list.")
                    pass
            todo = input("What do you want to change it to? ")
            todos[number - 1] = todo
            save_todos(todos)
        elif user_action.startswith("exit"):
            break
        elif user_action.startswith("wipe"):
            todos = []
            save_todos(todos)
        else:
            print("Command is not valid")

    print("Bye")


if __name__ == "__main__":
    main()
