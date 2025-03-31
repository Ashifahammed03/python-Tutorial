import pandas as pd
import matplotlib.pyplot as plt

# Load sales data
df = pd.read_csv('sales.csv')

# 1) Toothpaste sales scatter plot
plt.scatter(df['month_number'], df['toothpaste'], color='blue', label='Toothpaste Sales')
plt.xlabel('Month Number')
plt.ylabel('Toothpaste Sales')
plt.title('Toothpaste Sales Data')
plt.legend()
plt.show()

# 2) Face cream and face wash sales bar chart
plt.bar(df['month_number'] - 0.2, df['facecream'], width=0.4, label='Face Cream', color='green')
plt.bar(df['month_number'] + 0.2, df['facewash'], width=0.4, label='Face Wash', color='orange')
plt.xlabel('Month Number')
plt.ylabel('Sales')
plt.title('Face Cream and Face Wash Sales Data')
plt.legend()
plt.show()

# 3) Total sales data for last year - Pie chart
total_sales = df[['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']].sum()
labels = total_sales.index
sizes = total_sales.values
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Total Sales Data for Last Year')
plt.show()
