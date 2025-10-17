from sqlalchemy.orm import Session
from backend import models, schemas

def create_todo(db: Session, todo: schemas.TodoCreate):
    db_todo = models.Todo(task=todo.task, done=False)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def get_todos(db: Session):
    return db.query(models.Todo).all()

def update_todo(db: Session, todo_id: int):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if db_todo:
        db_todo.done = not db_todo.done
        db.commit()
        db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, todo_id: int):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if db_todo:
        db.delete(db_todo)
        db.commit()
    return db_todo
