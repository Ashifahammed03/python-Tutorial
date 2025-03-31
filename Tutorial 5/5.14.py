import pandas as pd

# Create data
data = [
    [10001, 'Jack', 76, 88, 76],
    [10002, 'John', 77, 84, 79],
    [10003, 'Alex', 74, 79, 81]
]

# Create DataFrame
df = pd.DataFrame(data, columns=['Reg_no', 'Name', 'Sub_Mark1', 'Sub_Mark2', 'Sub_Mark3'])

# Write to CSV file
df.to_csv('students.csv', index=False)
print("Data written to students.csv")
