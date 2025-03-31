import pandas as pd

# Create a dataframe from a list of data
data = [['Alice', 24], ['Bob', 27], ['Charlie', 22]]
df = pd.DataFrame(data, columns=['Name', 'Age'])

df.set_index('Name', inplace=True)
print(df)
