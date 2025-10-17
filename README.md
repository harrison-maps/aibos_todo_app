#  AIbos To-Do App

A simple yet powerful **To-Do List Web App** built with **Streamlit (Frontend)** and **FastAPI (Backend)**.  
It allows users to **add**, **view**, **mark as done**, and **delete tasks** easily.

---

##  Features

- Add new tasks  
- Mark tasks as done / undone  
- Delete completed or unwanted tasks  
- Simple, clean interface built with Streamlit  
- Fast and efficient backend using FastAPI  


##  Tech Stack

- **Frontend:** Streamlit 
- **Backend:** FastAPI  
- **Database:** JSON file (local storage)  


### 1️ Clone the repository
```bash
git clone https://github.com/harrison-maps/aibos_todo_app.git
cd aibos_todo_app
## this is the app setup
aibos_todo_app/
│
├── backend/
│ ├── main.py # FastAPI entry point
│ ├── crud.py # Create, Read, Update, Delete logic
│ ├── models.py # Database models
│ ├── schemas.py # Pydantic schemas
│ └── database.py # Database connection setup
│
├── frontend/
│ └── app.py # Streamlit app UI
│
└── README.md


---

## ⚙️ How to Run
pip install -r requirements.txt


### start the Backend
```bash
cd backend
uvicorn main:app --reload

cd ..
streamlit run frontend/app.py

## Tech Stack

FastAPI – Backend framework

SQLAlchemy – ORM for database management

SQLite – Lightweight local database

Streamlit – Interactive frontend UI

### Future Improvements
Because i didnot have any knowlege of React i couldnt do this project with it, so in future i will use React for the front end
Add user authentication (login/signup)

Add deadlines and reminders

Sync with cloud database (Firebase or PostgreSQL)

## Author
SSEMPALA HARRISON SOLOMON
Completed: October 17, 2025
Built for submission and demonstration purposes.

## Quick Summary

This app shows how backend APIs and frontend interfaces communicate 
you can add, complete, or delete tasks in real-time using a modern Python stack.