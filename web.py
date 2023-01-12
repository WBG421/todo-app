import streamlit as st
from helpers import open_todos, write_todos

def main():
    todos = open_todos()

    st.title("Hello")
    st.write("You can use this app to increase productivity")

    for todo in todos:
        checkbox = st.checkbox(todo, key=todo)
        if checkbox:
            todos.remove(todo)
            write_todos(todos)
            del st.session_state[todo]
            st._rerun()

    st.text_input(label="Add todo", label_visibility="hidden",
                  placeholder="Add new todo...",
                  on_change=add_todo, key="new_todo")

    st.session_state

def add_todo():
    todo = st.session_state["new_todo"]
    todos = open_todos()
    todos.append(todo)
    write_todos(todos)

if __name__ == "__main__":
    main()