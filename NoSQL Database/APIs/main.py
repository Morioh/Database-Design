from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from typing import List, Optional
from bson import ObjectId
from bson.errors import InvalidId

app = FastAPI()

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['Applicant_Data_db']
collection = db['students']

# Pydantic models


class FinancialDetails(BaseModel):
    FinancialStanding: str
    FeeBalanceUSD: float
    TotalMonthlyIncome: float


class HouseholdDetails(BaseModel):
    StudentsInHousehold: int
    HouseholdSize: int
    HouseholdSupporters: int
    HouseholdDependants: int


class GrantDetails(BaseModel):
    ALUGrantStatus: str
    PreviousAlusiveGrantStatus: str
    ALUGrantAmount: float
    GrantRequested: float
    AmountAffordable: float
    GrantClassifier: str


class Student(BaseModel):
    AcademicStanding: str
    DisciplinaryStanding: str
    FinancialDetails: FinancialDetails
    HouseholdDetails: HouseholdDetails
    GrantDetails: GrantDetails


class StudentUpdate(BaseModel):
    AcademicStanding: Optional[str] = None
    DisciplinaryStanding: Optional[str] = None
    FinancialDetails: Optional["FinancialDetails"] = None
    HouseholdDetails: Optional["HouseholdDetails"] = None
    GrantDetails: Optional["GrantDetails"] = None

# Helper function to convert MongoDB document to dictionary


def student_helper(student) -> dict:
    return {
        "id": str(student["_id"]),
        "AcademicStanding": student["AcademicStanding"],
        "DisciplinaryStanding": student["DisciplinaryStanding"],
        "FinancialDetails": student["FinancialDetails"],
        "HouseholdDetails": student["HouseholdDetails"],
        "GrantDetails": student["GrantDetails"]
    }

# Create student


@app.post("/students/", response_model=Student)
async def create_student(student: Student):
    student = student.dict()
    new_student = collection.insert_one(student)
    created_student = collection.find_one({"_id": new_student.inserted_id})
    return student_helper(created_student)

# Read all students


@app.get("/students/", response_model=List[Student])
async def read_students():
    students = collection.find()
    return [student_helper(student) for student in students]

# Read a student by ID


@app.get("/students/{student_id}", response_model=Student)
async def read_student(student_id: str):
    try:
        student = collection.find_one({"_id": ObjectId(student_id)})
        if student is None:
            raise HTTPException(status_code=404, detail="Student not found")
        return student_helper(student)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid student ID")

# Update student


@app.put("/students/{student_id}", response_model=Student)
async def update_student(student_id: str, student_update: StudentUpdate):
    try:
        update_data = {k: v for k, v in student_update.dict().items()
                       if v is not None}
        if update_data:
            collection.update_one({"_id": ObjectId(student_id)}, {
                                  "$set": update_data})
        updated_student = collection.find_one({"_id": ObjectId(student_id)})
        if updated_student is None:
            raise HTTPException(status_code=404, detail="Student not found")
        return student_helper(updated_student)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid student ID")

# Delete student


@app.delete("/students/{student_id}")
async def delete_student(student_id: str):
    try:
        result = collection.delete_one({"_id": ObjectId(student_id)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Student not found")
        return {"message": "Student deleted successfully"}
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid student ID")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
