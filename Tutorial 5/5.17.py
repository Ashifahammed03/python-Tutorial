import pandas as pd

# Load student data
df = pd.read_csv('student.csv')

# 1) Find the average CGPA of the students
average_cgpa = df['CGPA'].mean()
print("Average CGPA:", average_cgpa)

# 2) Display details of all students having CGPA > 9
high_cgpa_students = df[df['CGPA'] > 9]
print("Students with CGPA > 9:\n", high_cgpa_students)

# 3) Display details of all CSE students with CGPA > 9
cse_high_cgpa_students = df[(df['Branch'] == 'CSE') & (df['CGPA'] > 9)]
print("CSE Students with CGPA > 9:\n", cse_high_cgpa_students)

# 4) Display details of student with maximum CGPA
max_cgpa_student = df[df['CGPA'] == df['CGPA'].max()]
print("Student with Maximum CGPA:\n", max_cgpa_student)

# 5) Display average CGPA of each branch
average_cgpa_by_branch = df.groupby('Branch')['CGPA'].mean()
print("Average CGPA by Branch:\n", average_cgpa_by_branch)
