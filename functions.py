import numpy as np
import pandas as pd


def load_student_data(filepath):
  """Loads student records from a CSV file using Pandas."""
  try:
    df = pd.read_csv(filepath)
    return df
  except FileNotFoundError:
    print(f"Error: The file '{filepath}' was not found.")
    return None


def calculate_performance_metrics(df):
  """Calculates total marks, average marks, assigns grades, and determines pass/fail status using NumPy and Pandas."""
  subject_cols = ['Maths', 'Science', 'English']

  # Using NumPy to calculate total and average marks across subject columns
  df['Total_Marks'] = df[subject_cols].sum(axis=1)
  df['Average_Marks'] = df[subject_cols].mean(axis=1)

  # Assigning Grades based on average marks
  def assign_grade(avg):
    if avg >= 85:
      return 'A'
    elif avg >= 70:
      return 'B'
    elif avg >= 55:
      return 'C'
    elif avg >= 40:
      return 'D'
    else:
      return 'F'

  df['Grade'] = df['Average_Marks'].apply(assign_grade)

  # Pass/Fail Condition: Pass if Average Marks >= 40 and no individual subject < 35
  def check_pass_fail(row):
    if row['Average_Marks'] >= 40 and (row[subject_cols] >= 35).all():
      return 'Pass'
    else:
      return 'Fail'

  df['Status'] = df.apply(check_pass_fail, axis=1)
  return df


def get_subject_statistics(df):
  """Calculates subject-wise performance averages using NumPy/Pandas."""
  subject_cols = ['Maths', 'Science', 'English']
  stats = {}
  for sub in subject_cols:
    stats[sub] = {
        'Mean': np.mean(df[sub]),
        'Highest': np.max(df[sub]),
        'Lowest': np.min(df[sub]),
    }
  return stats


def get_top_performers(df, n=3):
  """Identifies the top-performing students based on average marks."""
  return df.sort_values(by='Average_Marks', ascending=False).head(n)