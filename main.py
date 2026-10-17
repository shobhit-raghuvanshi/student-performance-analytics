from functions import (
    calculate_performance_metrics,
    get_subject_statistics,
    get_top_performers,
    load_student_data,
)


def main():
  print('=' * 60)
  print('       STUDENT PERFORMANCE ANALYTICS SYSTEM')
  print('=' * 60)

  # Step 1: Load Dataset
  file_path = 'students.csv'
  df = load_student_data(file_path)

  if df is None:
    return

  print(f'\n[INFO] Successfully loaded {len(df)} student records.\n')

  # Step 2: Process Data
  df = calculate_performance_metrics(df)

  # Step 3: Overall Summary Statistics
  print('--- OVERALL CLASS SUMMARY ---')
  overall_avg_marks = df['Average_Marks'].mean()
  total_students = len(df)
  passed_students = len(df[df['Status'] == 'Pass'])
  failed_students = total_students - passed_students

  print(f'Total Students      : {total_students}')
  print(f'Overall Class Average: {overall_avg_marks:.2f}')
  print(f'Total Passed        : {passed_students}')
  print(f'Total Failed        : {failed_students}')

  # Step 4: Subject-wise Analysis
  print('\n--- SUBJECT-WISE PERFORMANCE ANALYSIS ---')
  subject_stats = get_subject_statistics(df)
  for sub, stats in subject_stats.items():
    print(
        f'Subject: {sub:<10} | Average: {stats["Mean"]:.2f} | Highest:'
        f' {stats["Highest"]} | Lowest: {stats["Lowest"]}'
    )

  # Step 5: Top Performers
  print('\n--- TOP 3 PERFORMING STUDENTS ---')
  top_students = get_top_performers(df, 3)
  for index, row in top_students.iterrows():
    print(
        f"Name: {row['Name']:<18} | Dept: {row['Department']:<25} | Average:"
        f" {row['Average_Marks']:.2f} | Grade: {row['Grade']}"
    )

  # Step 6: Detailed Processed Data Preview
  print('\n--- PROCESSED DATA PREVIEW (First 5 Rows) ---')
  print(
      df[[
          'StudentID',
          'Name',
          'Department',
          'Total_Marks',
          'Average_Marks',
          'Grade',
          'Status',
      ]].head()
  )
  print('=' * 60)


if __name__ == '__main__':
  main()