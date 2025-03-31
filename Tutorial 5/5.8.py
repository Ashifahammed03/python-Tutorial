import pandas as pd

df = pd.read_csv('auto.csv')

# 1) Clean and update the CSV file
df.dropna(inplace=True)  # Remove missing values
df.to_csv('auto_cleaned.csv', index=False)

# 2) Find the most expensive car company name
most_expensive = df[df['price'] == df['price'].max()]['company'].values[0]
print("Most expensive car company:", most_expensive)

# 3) Print all Toyota car details
toyota_cars = df[df['company'].str.lower() == 'toyota']
print("Toyota Car Details:\n", toyota_cars)

# 4) Print total cars of all companies
total_cars = df['company'].value_counts()
print("Total cars by company:\n", total_cars)

# 5) Find the highest priced car of all companies
highest_priced_cars = df.loc[df.groupby('company')['price'].idxmax()]
print("Highest priced cars:\n", highest_priced_cars)

# 6) Find the average mileage of all companies
average_mileage = df.groupby('company')['average-mileage'].mean()
print("Average mileage by company:\n", average_mileage)

# 7) Sort all cars by Price column
df_sorted = df.sort_values(by='price', ascending=False)
print("Cars sorted by price:\n", df_sorted)
