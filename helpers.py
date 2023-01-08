FILEPATH = "todos.txt"


def open_todos(filepath=FILEPATH):
    try:
        with open(filepath) as file_local:
            todos_local = [line.strip() for line in file_local]
    except FileNotFoundError:
        todos_local = []
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, "w") as file_local:
        for todo in todos_arg:
            file_local.write(f"{todo}\n")
    return

