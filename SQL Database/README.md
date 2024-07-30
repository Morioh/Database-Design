# Alusive Grant Application Dataset

## The data contains the following columns:

- **Academic Standing**: The academic performance of the student.
- **Disciplinary Standing**: The disciplinary record of the student.
- **Financial Standing**: The financial situation of the student.
- **Fee Balance (USD)**: The remaining fee balance the student needs to pay.
- **ALU Grant Status**: The status of the student's ALU awarded grant.
- **Previous Alusive Grant Status**: The status of any previous grants received from Alusive Africa.
- **Total Monthly Income**: The total monthly income of the student's household.
- **Students in Household**: The number of students in the student's household.
- **Household Size**: The total number of members in the student's household.
- **Household Supporters**: The number of people in the household who are financially supporting the family.
- **Household Dependants**: The number of dependents in the student's household.
- **ALU Grant Amount**: The amount of grant received from ALU.
- **Grant Requested**: The amount of grant requested by the student.
- **Amount Affordable**: The amount the student can afford to pay.
- **Grant Classifier**: The classification of the grant award status based on the provided data.

## Schema Table

- **Students Table** : Has a primary key StudentID.
- **FinancialDetails Table**: Uses StudentID as both a foreign key and primary key.
- **HouseholdDetails Table**: Uses StudentID as both a foreign key and primary key.
- **GrantDetails Table**: Uses StudentID as both a foreign key and primary key.

### Table 1: Students

    Student ID (PK)
    Academic Standing
    Disciplinary Standing

### Table 2: FinancialDetails

    Student ID (Composite Key)
    Financial Stadning
    FeeBalanceUSD
    TotalMonthlyIncome

### Table 3: HouseholdDetails

    Student ID (Composite Key)
    StudentInHousehold
    HouseholdSize
    HouseholdSupporters
    HouseholdDependants

### Table 4: GrantDetails

    Student ID (Composite Key)
    ALUGrantStatus
    PreviousAlusiveGrantStatus
    ALUGrantAmount
    GrantRequested
    AmountAffordable
    GrantClassification


**Note** :- The Database of choice here is **PostgreSQL**

## Database ER Diagram

### Relationship Type:

The kind of relationship here is a one-to-one relationship between the Students table and each of the other tables (FinancialDetails, HouseholdDetails, GrantDetails).

                One-to-One Relationship

	•	Each student in the Students table can have only one corresponding entry in the FinancialDetails table, one in the HouseholdDetails table, and one in the GrantDetails table.
	•	This is enforced by using the StudentID as both the primary key and foreign key in the related tables. This ensures that each related table entry corresponds to a unique student.
Here is the database ER Diagram

![](<Student ER Diagram.png>)