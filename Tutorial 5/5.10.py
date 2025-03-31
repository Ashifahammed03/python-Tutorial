import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'rollno': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'place': ['NY', 'LA', 'SF', 'TX', 'FL'],
    'mark': [85, 78, 92, 88, 76]
}
df = pd.DataFrame(data)
df.to_csv('stud.csv', index=False)

# a) Read and display the file contents
df = pd.read_csv('stud.csv')
print(df)

# b) Set rollno as index
df.set_index('rollno', inplace=True)
print(df)

# c) Display name and mark
print(df[['name', 'mark']])

# d) rollno, Name, and mark in the order of name
print(df[['name', 'mark']].sort_values(by='name'))

# e) Display the rollno, name, mark in descending order of mark
print(df[['name', 'mark']].sort_values(by='mark', ascending=False))

# f) Find the average mark, median, and mode
print("Average Mark:", df['mark'].mean())
print("Median Mark:", df['mark'].median())
print("Mode Mark:", df['mark'].mode()[0])

# g) Find minimum and maximum marks
print("Minimum Mark:", df['mark'].min())
print("Maximum Mark:", df['mark'].max())

# h) Variance and standard deviation of marks
print("Variance:", df['mark'].var())
print("Standard Deviation:", df['mark'].std())

# i) Display the histogram of marks
plt.hist(df['mark'], bins=5, edgecolor='black')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.title('Histogram of Marks')
plt.show()

# j) Remove the place column
df.drop(columns=['place'], inplace=True)
print(df)
