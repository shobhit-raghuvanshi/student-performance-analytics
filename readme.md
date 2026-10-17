# Student Performance Analytics System

## 1. Project Title & Details
* **Project Title:** Student Performance Analytics System
* **Technology Stack:** Python, NumPy, Pandas

## 2. Objective
The objective of this project is to build an automated data-analysis pipeline to ingest student academic records, process marks and attendance using NumPy and Pandas, and generate insightful metrics including total marks, averages, grades, pass/fail status, subject-wise statistics, and top performers.

## 3. Technologies Used
* **Python:** Core logic, loops, modular functions, and conditions.
* **Pandas:** DataFrame creation, data cleaning, filtering, and summary metrics.
* **NumPy:** Fast numerical vector operations (mean, min, max, sums).

## 4. Dataset Description (`students.csv`)
The dataset contains 16 student records across various engineering departments. Key columns include:
* `StudentID`: Unique identification number for each student.
* `Name`: Full name of the student.
* `Department`: Academic department (e.g., Computer Science, Mechanical).
* `Maths`, `Science`, `English`: Marks obtained out of 100.
* `Attendance`: Percentage attendance of the student.

## 5. Implementation Steps
1. **Data Loading:** Pandas reads `students.csv` into a structured DataFrame.
2. **Data Processing:** Functions iterate through rows/columns applying conditional logic, computing total and average marks via NumPy, allocating letter grades, and establishing pass/fail statuses.
3. **Statistical Analysis:** Evaluates class-wide averages, subject performance bounds (highest/lowest), and isolates top performers.
4. **Output Generation:** Structured console prints display clean summary insights.

## 6. Key Features
* Automated total and average score calculation.
* Dynamic grade assignment (`A`, `B`, `C`, `D`, `F`) based on threshold rules.
* Robust pass/fail determination checking both average scores and minimum passing thresholds.
* Subject-wise comparative performance analytics.
* Identification of top-ranking students.

## 7. Final Outcome
The system successfully processes raw CSV student data, performs vectorized calculations using NumPy/Pandas, and presents clean academic performance summaries without requiring manual intervention.

## 8. Challenges & Learning
* **Challenge:** Handling clean conditional checks for both overall average and individual subject minimum marks.
* **Solution:** Leveraged Pandas boolean indexing combined with NumPy aggregation methods.
* **Learning:** Gained hands-on experience structuring modular Python code, integrating Pandas DataFrames, and writing production-ready documentation for Git repositories.

## 9. GitHub Repository
https://github.com/shobhit-raghuvanshi/student-performance-analytics