# -------------------------------
# DATA VISUALIZATION WITH MATPLOTLIB
# -------------------------------
# Matplotlib is a Python library used for creating static, animated, 
# and interactive visualizations.
# The goal of data visualization is to make data easier to interpret,
# allowing users to identify patterns, trends, and outliers quickly.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from numpy import random


# 1. SCATTER AND LINE PLOT
# Load dataset
data = pd.read_csv('https://raw.githubusercontent.com/yash240990/Python/master/Grade_Set_1.csv')
print(data.head())

# Scatter plot of Hours_Studied vs Test_Grade
plt.scatter(data.Hours_Studied, data.Test_Grade, color='green')
plt.plot(data.Hours_Studied, data.Test_Grade, color='blue', label='Time Study')  # Line connecting points
plt.xlabel('Hours of study', fontsize=12)
plt.ylabel('Grade Test', fontsize=12)
plt.title('Hours studied VS Test grade')
plt.legend()
plt.show()


# 2. XTICKS AND YTICKS EXAMPLES
# Basic line plot
x = random.randint(100, size=10)
y = random.randint(50, size=10)
plt.plot(x, y, color='blue')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Xticks and Yticks')
plt.show()

# Line plot with custom xticks and yticks
x = random.randint(100, size=10)
y = random.randint(50, size=10)
plt.plot(x, y, color='blue')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Xticks and Yticks')
plt.xticks(np.arange(0, 100, 5))  # Custom X-axis ticks from 0 to 100 with step 5
plt.yticks(np.arange(0, 60, 5))   # Custom Y-axis ticks from 0 to 60 with step 5
plt.show()


# 3. HISTOGRAM
# Histograms show the distribution of data by dividing it into bins
ages = [18, 21, 22, 25, 26, 30, 34, 35, 36, 40, 42, 45, 46, 50]
plt.hist(ages, bins=5, color='red', edgecolor='black')  # edgecolor to separate bins
plt.title('Age Distribution')
plt.xlabel('Age of buyer')
plt.ylabel('Frequency of purchased')
plt.xticks(np.arange(18, 51, 6))
plt.show()


# 4. HEATMAP (CORRELATION MATRIX)
data_dict = { 
    'hours_studied': [2,3,4,5,6,7,8],
    'Marks_scored': [30,40,50,60,70,80,90],
    'Tv_watched': [10,9,8,7,6,5,4]
}
df = pd.DataFrame(data_dict)

# Compute correlation
corr = df.corr()

# Heatmap visualization
sb.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Heatmap')
plt.show()

# Check correlation values
print(df.corr())


# 5. SUBPLOTS (MULTIPLE GRAPHS IN ONE FIGURE)
# Example: 1 row, 2 columns
x1 = random.randint(10, size=(7))
y1 = random.randint(6, size=(7))
plt.subplot(1, 2, 1)
plt.plot(x1, y1, color='green')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Plot 1')

x2 = random.randint(20, size=(7))
y2 = random.randint(10, size=(7))
plt.subplot(1, 2, 2)
plt.plot(x2, y2, color='red')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Plot 2')
plt.show()


# 6. SUBPLOTS (2 ROWS, 3 COLUMNS)
for i in range(6):
    x = random.randint(10, size=(7))
    y = random.randint(6, size=(7))
    plt.subplot(2, 3, i+1)
    color_list = ['green', 'blue', 'red', 'purple', 'black', 'orange']
    if i == 4:
        plt.scatter(x, y, color=color_list[i])
    else:
        plt.plot(x, y, color=color_list[i])
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.title(f'Plot {i+1}')

# Adjust layout to avoid overlap
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.4)
plt.show()


# 7. MULTIPLE LINE PLOTS IN ONE FIGURE
plt.figure(figsize=(12, 6))
colors = ['green', 'red', 'blue', 'purple', 'orange', 'brown']
xa = [3,1,1,2,3,4,5,5,5,3]
ya = [1,5,6,7,6,7,6,5,5,1]

# Loop to create 6 subplots in 2x3 layout
for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.plot(xa, ya, color=colors[i])
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.grid(True)
    plt.title(f'Plot {i + 1}')

plt.tight_layout()
plt.show()
