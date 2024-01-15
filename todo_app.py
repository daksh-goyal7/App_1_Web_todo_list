import streamlit as st
import function

todos=function.get_todos()

def add_todo():
    todo=st.session_state["new_todo"]+"\n"
    todos.append(todo)
    function.write_todos(todos)

st.title("My to-do app")
st.subheader("Check list of to-do")

for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="",placeholder="Enter to do here",on_change=add_todo,key="new_todo")
st.session_state
