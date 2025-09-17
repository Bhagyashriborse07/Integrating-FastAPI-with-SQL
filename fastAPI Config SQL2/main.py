from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create Employee
@app.post("/employees/", response_model=schemas.Employee)
def create_employee(emp: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, emp)

# Get All Employees
@app.get("/employees/", response_model=list[schemas.Employee])
def read_employees(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_employees(db, skip, limit)

# Get Employee by ID
@app.get("/employees/{emp_id}", response_model=schemas.Employee)
def read_employee(emp_id: int, db: Session = Depends(get_db)):
    emp = crud.get_employee(db, emp_id)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp

# Update Employee
@app.put("/employees/{emp_id}", response_model=schemas.Employee)
def update_employee(emp_id: int, emp: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    updated_emp = crud.update_employee(db, emp_id, emp)
    if not updated_emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return updated_emp

# Delete Employee
@app.delete("/employees/{emp_id}", response_model=schemas.Employee)
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    deleted_emp = crud.delete_employee(db, emp_id)
    if not deleted_emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return deleted_emp
