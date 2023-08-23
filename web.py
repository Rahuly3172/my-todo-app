import streamlit as st
import functions

# to run
# python -m streamlit run your_script.py

# to connect
# pip freeze > requirements.txt


todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"]+"\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("this is my todo app")
st.text("this app increases your productivity")
for i in todos:
    checkbox = st.checkbox(f"{i}.", key=i)
    if checkbox:
        index = todos.index(i)
        print(index)
        print(f"the todo {i}")
        print(checkbox)
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[i]
        st._rerun()
        # todos.append(index)
        # print(todos[index])
        # functions.write_todos(todos)


st.text_input(label="Enter a todo",
              placeholder="Add new todo",
              on_change=add_todo, key="new_todo")
# st.session_state

