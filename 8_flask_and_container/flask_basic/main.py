from flask import Flask,request
from student import Student
app = Flask(__name__)


@app.get("/")
def homePage():
    return "hello this is homepage"

@app.get("/student")
def get_student():
    return "here is student A."    


@app.post("/add_student")
def add_student():
    request_data = request.json
    
    stu_obj = Student(name = request_data["stu_name"],
    subjects=request_data["stu_subjects"],marks= request_data["stu_marks"])
    write_tofile(stu_obj=stu_obj)
    return request_data


def write_tofile(stu_obj:Student):
    print(stu_obj.print_stu())




app.run(debug=False, host="0.0.0.0",port = 8080)