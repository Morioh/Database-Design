-- Table to store basic student information
CREATE TABLE Students (
    StudentID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each student
    AcademicStanding VARCHAR(50), -- Academic performance of the student
    DisciplinaryStanding VARCHAR(50) -- Disciplinary record of the student
);

-- Table to store financial details related to students
CREATE TABLE FinancialDetails (
    StudentID INT, -- Foreign key to reference the Students table
    FinancialStanding VARCHAR(50), -- Financial situation of the student
    FeeBalanceUSD DECIMAL(10, 2), -- Remaining fee balance in USD
    TotalMonthlyIncome DECIMAL(10, 2), -- Total monthly income of the student's household
    PRIMARY KEY (StudentID), -- Primary key, ensuring each entry is unique and references a student
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) -- Foreign key constraint
);

-- Table to store household details related to students
CREATE TABLE HouseholdDetails (
    StudentID INT, -- Foreign key to reference the Students table
    StudentsInHousehold INT, -- Number of students in the household
    HouseholdSize INT, -- Total number of members in the household
    HouseholdSupporters INT, -- Number of people financially supporting the household
    HouseholdDependants INT, -- Number of dependents in the household
    PRIMARY KEY (StudentID), -- Primary key, ensuring each entry is unique and references a student
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) -- Foreign key constraint
);

-- Table to store grant details related to students
CREATE TABLE GrantDetails (
    StudentID INT, -- Foreign key to reference the Students table
    ALUGrantStatus VARCHAR(50), -- Status of the ALU awarded grant
    PreviousAlusiveGrantStatus VARCHAR(50), -- Status of previous grants from Alusive Africa
    ALUGrantAmount DECIMAL(10, 2), -- Amount of grant received from ALU
    GrantRequested DECIMAL(10, 2), -- Amount of grant requested by the student
    AmountAffordable DECIMAL(10, 2), -- Amount the student can afford to pay
    GrantClassifier VARCHAR(50), -- Classification of the grant award status
    PRIMARY KEY (StudentID), -- Primary key, ensuring each entry is unique and references a student
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) -- Foreign key constraint
);