# to run fastAPI code uvicorn main:app --reload
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()    
          
 #creating your own datatype ,i.e. equivalent to struct in C
class Mydatatype(BaseModel):
    name:str
    number:int
    nickname:str

students=[] 

@app.get("/")
def hello():
    return "WELCOME TO FASTAPI"


@app.get("/home/{name}/{id}")
def home(name:str,id:int):
    return {"name":name,"ID":id}


@app.post("/add")
def add_student(details:Mydatatype):
    students.append(details.dict())
    return details

@app.delete("/del")
def del_student():
    students.pop(-1)
    return "Task done."    
