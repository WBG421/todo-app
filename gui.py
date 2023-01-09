from helpers import open_todos, write_todos
import PySimpleGUI as sg

label = sg.Text("Type in to-do")
input_box = sg.InputText(tooltip="Enter to do", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=open_todos(), key="todos",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")

window = sg.Window("To-Do App",
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=("Arial", 14))
while True:
    event, values = window.read()
    print(event, values)
    match event:
        case "Add":
            todos = open_todos()
            new_todo = values["todo"]
            todos.append(new_todo)
            write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]
            todos = open_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            write_todos(todos)
            window["todos"].update(values=todos)
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case sg.WIN_CLOSED:
            break

window.close()
