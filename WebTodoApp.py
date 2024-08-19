import streamlit as st
import functions

# retrieve the todos from the todo.txt file through get_todos() from functions.py
todos = functions.get_todos()


def add_todo_fn():
    entered_todo = st.session_state["new_todo_key"]+'\n'
    todos.append(entered_todo)
    functions.write_todos(todos)
    # print(entered_todo)
    # print("session_state:", st.session_state)


st.title('My Todo App')
# st.subheader('This is my Todo App')
# st.write("This app increases your focus & productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label='Todo:', label_visibility='hidden',
              placeholder = 'Enter here the new Todo:',
              on_change=add_todo_fn,
              key="new_todo_key")

st.session_state

# print('Hello')

