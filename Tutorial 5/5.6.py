import pandas as pd

# Create data
data = [
    [1, 'Linus Torvalds', 'Finland', 'Linux Kernel', 1991],
    [2, 'Tim Berners-Lee', 'England', 'World Wide Web', 1990],
    [3, 'Guido van Rossum', 'Netherlands', 'Python', 1991]
]

# Create DataFrame
df = pd.DataFrame(data, columns=['SN', 'Name', 'Country', 'Contribution', 'Year'])

# Write to CSV file
df.to_csv('contributors.csv', index=False)
print("Data written to contributors.csv")
