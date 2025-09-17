from pydantic import BaseModel

class EmployeeBase(BaseModel):
    name: str
    email: str
    department: str
    is_active: bool = True

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int

    class Config:
        orm_mode = True
