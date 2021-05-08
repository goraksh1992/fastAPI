from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

fakedb = []

class Courses(BaseModel):
    id: int
    name: str
    price: int
    is_free: Optional[bool] = None

@app.get("/")
def get_courses():
    return fakedb

@app.post('/add-course')
def add_course(course: Courses):
    fakedb.append(course.dict())
    return fakedb[-1]

@app.delete('/delete-course/{course_id}')
def delete_course(course_id: int):
    fakedb.pop(course_id-1)
    return {"msg": "Course deleted!"}
