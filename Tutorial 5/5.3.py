import pandas as pd

data = [['Alice', 24], ['Bob', 27], ['Charlie', 22]]
df = pd.DataFrame(data, columns=['Name', 'Age'])

df.to_excel('data.xlsx', index=False)
print("Data written to data.xlsx")
