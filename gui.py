from helpers import open_todos,write_todos
import PySimpleGUI as sg

label = sg.Text("Type in to-do")
input_box = sg.InputText(tooltip="Enter to do", key="todo")
add_button = sg.Button("Add")

window = sg.Window("To-Do App",
                   layout=[[label], [input_box, add_button]],
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
        case sg.WIN_CLOSED:
            break

window.close()

