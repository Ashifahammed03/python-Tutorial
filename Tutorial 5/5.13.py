import pandas as pd

# Load employee data
df = pd.read_csv('employee.csv')

# 1) Print first 7 records
print(df.head(7))

# 2) Print all employee names in alphabetical order
print(df['name'].sort_values())

# 3) Find the name of the employee with the highest salary
highest_paid = df[df['salary'] == df['salary'].max()]['name'].values[0]
print("Employee with highest salary:", highest_paid)

# 4) List the names of male employees
male_employees = df[df['gender'].str.lower() == 'male']['name']
print("Male Employees:\n", male_employees)

# 5) Display all unique teams employees belong to
print("Teams:\n", df['team'].unique())
