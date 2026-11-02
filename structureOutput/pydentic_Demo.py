from pydantic import BaseModel

class Student(BaseModel):
    name:str
    class_name:str
    age:int

new_student = {"name":"mavi", "class_name":"10th", "age":15}    

student= Student(**new_student)
print(student)