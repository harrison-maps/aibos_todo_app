from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from backend import crud, schemas, models
from backend.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/todos/", response_model=schemas.Todo)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db=db, todo=todo)

@app.get("/todos/", response_model=list[schemas.Todo])
def read_todos(db: Session = Depends(get_db)):
    return crud.get_todos(db)

@app.put("/todos/{todo_id}", response_model=schemas.Todo)
def update_todo(todo_id: int, db: Session = Depends(get_db)):
    return crud.update_todo(db, todo_id)

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    return crud.delete_todo(db, todo_id)
