from fastapi import FastAPI

app = FastAPI()

grades = {
"1": {"name": "Moshe", "grade": 88},
"2": {"name": "Yaakov", "grade": 75},
"3": {"name": "David", "grade": 92},
}



@app.get("/student")
def all_student():
    return grades


@app.get("/student/top")
def get_top():
    return max(grades.values(), key=lambda x: x["grade"])


@app.get("/students/averag")
def get_average():
    if grades:
        count = 0 
        sum_grende = 0
        for grade in grades.values():
            count +=1
            sum_grende += grade["grade"]
        return{"average": sum_grende/count}   

@app.get("/students/count")
def get_count():
    return {"count": len(grades)}    


@app.get("/students/{student_id}")
def get_student_id(student_id):
    return grades[student_id]
    