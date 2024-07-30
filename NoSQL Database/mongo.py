import pandas as pd
from pymongo import MongoClient

# Load the dataset
file_path = './Applicant_Data.csv'
applicant_data = pd.read_csv(file_path)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
# Create the database named 'Applicant_Data_db'
db = client['Applicant_Data_db']
collection = db['students']  # Create the collection named 'students'

# Insert data into MongoDB
for index, row in applicant_data.iterrows():
    student_document = {
        "AcademicStanding": row['Academic Standing'],
        "DisciplinaryStanding": row['Disciplinary Standing'],
        "FinancialDetails": {
            "FinancialStanding": row['Financial Standing'],
            "FeeBalanceUSD": row['Fee Balance (USD)'],
            "TotalMonthlyIncome": row['Total Monthly Income']
        },
        "HouseholdDetails": {
            "StudentsInHousehold": row['Students in Household'],
            "HouseholdSize": row['Household Size'],
            "HouseholdSupporters": row['Household Supporters'],
            "HouseholdDependants": row['Household Dependants']
        },
        "GrantDetails": {
            "ALUGrantStatus": row['ALU Grant Status'],
            "PreviousAlusiveGrantStatus": row['Previous Alusive Grant Status'],
            "ALUGrantAmount": row['ALU Grant Amount'],
            "GrantRequested": row['Grant Requested'],
            "AmountAffordable": row['Amount Affordable'],
            "GrantClassifier": row['Grant Classifier']
        }
    }
    collection.insert_one(student_document)

# Close the connection
client.close()
