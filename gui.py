import PySimpleGUI as sg

label = sg.Text("Type in to-do")
input_box = sg.InputText(tooltip="Enter to do")
add_button = sg.Button("Add")

window = sg.Window("To-Do App", layout=[[label], [input_box, add_button]])
window.read()
window.close()
