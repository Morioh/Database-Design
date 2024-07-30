import requests
import pandas as pd
import joblib
import numpy as np

# Define the API endpoint
API_URL = "http://localhost:8000/students/"

# Function to fetch the latest student entry


def fetch_latest_student():
    response = requests.get(API_URL)
    if response.status_code == 200:
        students = response.json()
        if students:
            # Assuming students are returned in ascending order by creation time, fetch the last student
            latest_student = students[-1]
            return latest_student
        else:
            raise ValueError("No students found in the database")
    else:
        raise ValueError(
            f"Error fetching data from API: {response.status_code}")

# Load the model


def load_model(model_path):
    return joblib.load(model_path)

# Prepare the data for prediction


def prepare_data(student):
    data = {
        "AcademicStanding": student["AcademicStanding"],
        "DisciplinaryStanding": student["DisciplinaryStanding"],
        "FinancialStanding": student["FinancialDetails"]["FinancialStanding"],
        "FeeBalanceUSD": student["FinancialDetails"]["FeeBalanceUSD"],
        "TotalMonthlyIncome": student["FinancialDetails"]["TotalMonthlyIncome"],
        "StudentsInHousehold": student["HouseholdDetails"]["StudentsInHousehold"],
        "HouseholdSize": student["HouseholdDetails"]["HouseholdSize"],
        "HouseholdSupporters": student["HouseholdDetails"]["HouseholdSupporters"],
        "HouseholdDependants": student["HouseholdDetails"]["HouseholdDependants"],
        "ALUGrantStatus": student["GrantDetails"]["ALUGrantStatus"],
        "PreviousAlusiveGrantStatus": student["GrantDetails"]["PreviousAlusiveGrantStatus"],
        "ALUGrantAmount": student["GrantDetails"]["ALUGrantAmount"],
        "GrantRequested": student["GrantDetails"]["GrantRequested"],
        "AmountAffordable": student["GrantDetails"]["AmountAffordable"],
        "GrantClassifier": student["GrantDetails"]["GrantClassifier"]
    }
    df = pd.DataFrame([data])
    return df

# Make predictions


def make_predictions(model, input_data):
    predictions = model.predict(input_data)
    return predictions


def main():
    # Fetch the latest student entry
    latest_student = fetch_latest_student()
    print("Latest student entry fetched successfully")

    # Load the pre-trained model
    model = load_model('grant_classifier_V2.pkl')
    print("Model loaded successfully")

    # Prepare the input data
    input_data = prepare_data(latest_student)
    print("Data prepared for prediction")

    # Make predictions
    predictions = make_predictions(model, input_data)

    # if the prediction is 1, the applicant is qualified for the grant; otherwise, the applicant is not
    if prediction == 1:
        prediction = "Qualified"
    else:
        prediction = "Not Qualified"
    print(f"Predictions: {predictions}")


if __name__ == "__main__":
    main()
