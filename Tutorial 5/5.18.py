import pandas as pd
import matplotlib.pyplot as plt

# Load weather data
df = pd.read_csv('weather.csv')

# 1) Print first 10 rows of weather data
print(df.head(10))

# 2) Find the maximum and minimum temperature
max_temp = df['temperature'].max()
min_temp = df['temperature'].min()
print("Maximum Temperature:", max_temp)
print("Minimum Temperature:", min_temp)

# 3) List the places with temperature less than 28°C
cool_places = df[df['temperature'] < 28]['place'].unique()
print("Places with Temperature < 28°C:", cool_places)

# 4) List the places with weather = 'Cloudy'
cloudy_places = df[df['weather'] == 'Cloudy']['place'].unique()
print("Places with Cloudy Weather:", cloudy_places)

# 5) Sort and display each weather type and its frequency
weather_counts = df['weather'].value_counts()
print("Weather Frequency:\n", weather_counts)

# 6) Create a bar plot to visualize temperature of each day
plt.figure(figsize=(10,5))
plt.bar(df['date'], df['temperature'], color='skyblue')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Variation Over Days')
plt.xticks(rotation=45)
plt.show()
