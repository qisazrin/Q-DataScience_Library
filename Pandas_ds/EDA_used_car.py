import pandas as pd
import numpy as np
import matplotlib.pyplot as mb
import seaborn as sb
import warnings
from datetime import date

warnings.filterwarnings('ignore')

# Load dataset
data = pd.read_csv('https://raw.githubusercontent.com/yashy1626/ds_dataset/refs/heads/main/used_cars.csv')
data

# first 20 rows of dataset
data.head(20)

# check for original data
data.info()

# calculate number of unique values
data.nunique()

# calculate percentage of null values in the data
(data.isnull().sum() / len(data)) * 100

# missing values in New_Price is 86% and Price 17%
# data Reduction, drop any unpredictable data
data = data.drop(['S.No.'], axis=1)
data.info()

# add column that shows year of manufacturing
data['Car_Age'] = date.today().year - data['Year']
data.head(20)

# extract Brand and Model from Name
data['Brand'] = data.Name.str.split().str.get(0)
data['Model'] = data.Name.str.split().str.get(1) + data.Name.str.split().str.get(2)
data[['Name', 'Brand', 'Model']]

# find duplicate values
print(data.Brand.unique())
print(data.Brand.nunique())

# check inconsistent brand names
searchfor = ['Isuzu','ISUZU','Mini','Land']
data[data.Brand.str.contains('|'.join(searchfor))].head()

# convert string columns to numeric where possible
columns = ['Mileage','Engine', 'Power']
for i in columns:
    data[i] = data[i].astype(str).str.extract(r'([\d.]+)').astype(float)
data

# Data Analysis
data.describe(include='all').T

# separate numerical and categorical variables
num_col = data.select_dtypes(include=np.number).columns.tolist()
cat_col = data.select_dtypes(include=['object']).columns.tolist()
print('Numerical Variables :')
print(num_col)
print('Categorical Variables :')
print(cat_col)

# Univariate Analysis for numerical variables
for i in num_col:
    print(i)
    print('Skew :', round(data[i].skew(), 2))
    mb.figure(figsize=(8, 4))
    data[i].hist(grid=False, bins=15)
    mb.title(f'Distribution of {i}')
    mb.xlabel(i)
    mb.ylabel('Count')
    mb.show()
    mb.tight_layout()

# Univariate Analysis for categorical variables
fig, axes = mb.subplots(3, 2, figsize = (18, 18))
fig.suptitle('Bar plot for all categorical variables in the dataset')

sb.countplot(ax = axes[0, 0], x = 'Fuel_Type', data = data, color = 'red', order = data['Fuel_Type'].value_counts().index)
sb.countplot(ax = axes[0, 1], x = 'Transmission', data = data, color = 'blue', order = data['Transmission'].value_counts().index)
sb.countplot(ax = axes[1, 0], x = 'Owner_Type', data = data, color = 'green', order = data['Owner_Type'].value_counts().index)
sb.countplot(ax = axes[1, 1], x = 'Location', data = data, color = 'orange', order = data['Location'].value_counts().index)
sb.countplot(ax = axes[2, 0], x = 'Brand', data = data, color = 'purple', order = data['Brand'].head(20).value_counts().index)
sb.countplot(ax = axes[2, 1], x = 'Model', data = data, color = 'pink', order = data['Model'].head(20).value_counts().index)

axes[1][1].tick_params(labelrotation=45)
axes[2][0].tick_params(labelrotation=90)
axes[2][1].tick_params(labelrotation=90)

# Log Transformation
def log_transform(data, col):
    for colname in col:
        if (data[colname] == 1.0).all():
            data[colname + '_log'] = np.log(data[colname] + 1)
        else:
            data[colname + '_log'] = np.log(data[colname])

log_transform(data, ['Kilometers_Driven','Price'])

# plot log transformed Kilometers_Driven
sb.distplot(data["Kilometers_Driven_log"], axlabel="Kilometers_Driven_log")


# Bivariate Analysis
mb.figure(figsize=(13,17))
sb.pairplot(data=data.drop(['Kilometers_Driven','Price'], axis=1))
mb.show()

# Categorical vs Continuous
fig, axarr = mb.subplots(4, 2, figsize=(12, 18))
data.groupby('Location')['Price_log'].mean().sort_values(ascending=False).plot.bar(ax=axarr[0][0], fontsize=12)
axarr[0][0].set_title("Location Vs Price", fontsize=18)

data.groupby('Transmission')['Price_log'].mean().sort_values(ascending=False).plot.bar(ax=axarr[0][1], fontsize=12)
axarr[0][1].set_title("Transmission Vs Price", fontsize=18)

data.groupby('Fuel_Type')['Price_log'].mean().sort_values(ascending=False).plot.bar(ax=axarr[1][0], fontsize=12)
axarr[1][0].set_title("Fuel_Type Vs Price", fontsize=18)

data.groupby('Owner_Type')['Price_log'].mean().sort_values(ascending=False).plot.bar(ax=axarr[1][1], fontsize=12)
axarr[1][1].set_title("Owner_Type Vs Price", fontsize=18)

data.groupby('Brand')['Price_log'].mean().sort_values(ascending=False).head(10).plot.bar(ax=axarr[2][0], fontsize=12)
axarr[2][0].set_title("Brand Vs Price", fontsize=18)

data.groupby('Model')['Price_log'].mean().sort_values(ascending=False).head(10).plot.bar(ax=axarr[2][1], fontsize=12)
axarr[2][1].set_title("Model Vs Price", fontsize=18)

data.groupby('Seats')['Price_log'].mean().sort_values(ascending=False).plot.bar(ax=axarr[3][0], fontsize=12)
axarr[3][0].set_title("Seats Vs Price", fontsize=18)

data.groupby('Car_Age')['Price_log'].mean().sort_values(ascending=False).plot.bar(ax=axarr[3][1], fontsize=12)
axarr[3][1].set_title("Car_Age Vs Price", fontsize=18)

mb.subplots_adjust(hspace=1.0)
mb.subplots_adjust(wspace=.5)
sb.despine()

# Multivariate Analysis
numeric_data = data.select_dtypes(include=['number'])
mb.figure(figsize=(12, 7))
sb.heatmap(numeric_data.corr(), cmap='magma', annot=True, vmin=-1, vmax=1)
mb.show()


# Impute Missing Values
data.loc[data["Mileage"] == 0.0, 'Mileage'] = np.nan
data['Mileage'].fillna(value=np.mean(data['Mileage']), inplace=True)

data['Seats'] = data.groupby(['Model', 'Brand'])['Seats'].transform(lambda x: x.fillna(x.median()))
data['Engine'] = data.groupby(['Brand', 'Model'])['Engine'].transform(lambda x: x.fillna(x.median()))
data['Power'] = data.groupby(['Brand', 'Model'])['Power'].transform(lambda x: x.fillna(x.median()))


# Insights (EDA Summary)
# Most customers prefer 2 Seat cars hence the price of the 2-seat cars is higher than other cars.
# The price of the car decreases as the Age of the car increases.
# Customers prefer to purchase First owner cars rather than Second or Third owner.
# Customers prefer Electric vehicles due to fuel price increase.
# Automatic Transmission is easier than Manual.
