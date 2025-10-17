import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000/todos/"

st.set_page_config(page_title="Todo App", page_icon="✅", layout="centered")
st.title(" AIBOS Todo App")

#  Add a new todo
st.subheader("Add New Task")
task = st.text_input("Task Name")

if st.button("➕ Add Todo"):
    if task:
        response = requests.post(BASE_URL, json={"task": task})
        if response.status_code == 200:
            st.success(" Todo added successfully!")
        else:
            st.error(" Failed to add todo.")
    else:
        st.warning("Please enter a task before adding.")

#  Show all todos
st.subheader("Your Tasks")
response = requests.get(BASE_URL)

if response.status_code == 200:
    todos = response.json()
    if not todos:
        st.info("No tasks yet. Add one above.")
    for todo in todos:
        col1, col2, col3 = st.columns([5, 1, 1])
        col1.write(f" **{todo['task']}** {'✅' if todo['done'] else '❌'}")
        
        if col2.button("🌀 Toggle", key=f"toggle_{todo['id']}"):
            requests.put(f"{BASE_URL}{todo['id']}")
            st.rerun()
        
        if col3.button("🗑️ Delete", key=f"delete_{todo['id']}"):
            requests.delete(f"{BASE_URL}{todo['id']}")
            st.rerun()
else:
    st.error("Failed to load todos from backend.")
