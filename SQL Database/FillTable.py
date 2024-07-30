# Import necessary libraries
import pandas as pd
import psycopg2

# Load the dataset
file_path = './Applicant_Data.csv'
applicant_data = pd.read_csv(file_path)

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="Applicant_Data_db",
    user="alu",
    password="123456789",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Insert data into Students table
for index, row in applicant_data.iterrows():
    cur.execute("""
        INSERT INTO Students (AcademicStanding, DisciplinaryStanding)
        VALUES (%s, %s) RETURNING StudentID;
    """, (row['Academic Standing'], row['Disciplinary Standing']))
    student_id = cur.fetchone()[0]

    # Insert data into FinancialDetails table
    cur.execute("""
        INSERT INTO FinancialDetails (StudentID, FinancialStanding, FeeBalanceUSD, TotalMonthlyIncome)
        VALUES (%s, %s, %s, %s);
    """, (student_id, row['Financial Standing'], row['Fee Balance (USD)'], row['Total Monthly Income']))

    # Insert data into HouseholdDetails table
    cur.execute("""
        INSERT INTO HouseholdDetails (StudentID, StudentsInHousehold, HouseholdSize, HouseholdSupporters, HouseholdDependants)
        VALUES (%s, %s, %s, %s, %s);
    """, (student_id, row['Students in Household'], row['Household Size'], row['Household Supporters'], row['Household Dependants']))

    # Insert data into GrantDetails table
    cur.execute("""
        INSERT INTO GrantDetails (StudentID, ALUGrantStatus, PreviousAlusiveGrantStatus, ALUGrantAmount, GrantRequested, AmountAffordable, GrantClassifier)
        VALUES (%s, %s, %s, %s, %s, %s, %s);
    """, (student_id, row['ALU Grant Status'], row['Previous Alusive Grant Status'], row['ALU Grant Amount'], row['Grant Requested'], row['Amount Affordable'], row['Grant Classifier']))

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
