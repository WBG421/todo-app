from helpers import open_todos, write_todos
import PySimpleGUI as sg
import time

clock = sg.Text("", key="clock")
label = sg.Text("Type in to-do")
input_box = sg.InputText(tooltip="Enter to do", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=open_todos(), key="todos",
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("To-Do App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Arial", 14))
while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%d %b %Y %H:%M:%S"))
    print(event, values)
    match event:
        case "Add":
            todos = open_todos()
            new_todo = values["todo"]
            todos.append(new_todo)
            write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
            except IndexError:
                sg.popup("Select an item first", font=("Arial", 14))
                continue
            new_todo = values["todo"]
            todos = open_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            write_todos(todos)
            window["todos"].update(values=todos)
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
            except IndexError:
                sg.popup("Select an item first", font=("Arial", 14))
                continue
            todos = open_todos()
            todos.remove(todo_to_complete)
            write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        case "Exit":
            break
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case sg.WIN_CLOSED:
            break

window.close()
