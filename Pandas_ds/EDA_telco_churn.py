import pandas as pd  # type: ignore
import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore
import seaborn as sb # type: ignore
import warnings
warnings.filterwarnings('ignore')
# case study
# john want us to analys his company telecom data and why lot of churn of the user.
#as his bestfriend who work as data science help him to deep analys his data.

# load dataset
data=pd.read_csv('https://raw.githubusercontent.com/harshbg/Telecom-Churn-Data-Analysis/master/Telecom%20Churn.csv')
data

# display the max number of rows and colomn # can used if needed, or the cells with run slow
#pd.options.display.max_columns = None
#pd.options.display.max_rows = None

#head()
# display first 5 rows of dataset   #data(name of var).head()
print(data.head())

#tail()
# display 5 rows of dataset
data.tail()

#PROPERTY
#colomns __> retrieves all the column names  
data.columns  

# shape __> returns the number of rows and columns
data.shape      

# info()
# shows complete summary of dataset
data.info()

# want to change dataset bool into integer    # only can load 1 time
data['churn']=data['churn'].astype('int')

# Describe()
# only shows the statistical summary of numerical features only
data.describe()

# generating statistical summary of non-numerical features
data.describe(include='object')

# value_counts()
# returns series containing count of unique value
data['international plan'].value_counts()

#use seaborn
sb.countplot(x='international plan',data=data)
plt.title('International Plan Summary')
plt.show()

# Missing value calculation
# isnull() used to identify null values in dataset
# Return TRUE if found any missing value
data.isnull().sum()  # show me sum of the data

#try assumption of customer service with churn user¶
data[['phone number','customer service calls','churn']].head()

#filter a DataFrame based on condition
data[data['customer service calls']>=4][['phone number','churn']].head(10)     

# sorting
#sort_values(by='.....')
data.sort_values(by='total day calls',ascending=False).head(10)

data.sort_values(by='total day minutes',ascending=False).head(10)
# while investigate by minutes lot of churn user that hv used services the most rather than other

#how much on a average active spend on phone during day time
print('Active User Spend On Phone During Day Time :',data[data['churn']==0]['total day minutes'].mean())
# how much on an average churn users spend on phone during day time
print('Churn User Spend On Phone During Day Time :',data[data['churn']==1]['total day minutes'].mean())
# how much on an average churn users spend on phone during night time
print('Churn User Spend On Phone During Night Time :',data[data['churn']==1]['total night minutes'].mean())
# how much on an average active users spend on phone during night time
print('Active User Spend On Phone During Night Time :',data[data['churn']==0]['total night minutes'].mean())
# how much on an average churn users spend on phone during evening time
print('Churn User Spend On Phone During Evening Time :',data[data['churn']==1]['total eve minutes'].mean())
# how much on an average active users spend on phone during evening time
print('Active User Spend On Phone During Evening Time :',data[data['churn']==0]['total eve minutes'].mean())

#much more easier use this method by compare it 2 table without use many code to get average(.mean())
# get the average values for churn user
data[data['churn']==1].mean(numeric_only=True)

# get the average values for active user
data[data['churn']==0].mean(numeric_only=True)

#grouping
columnsgrp=['total day minutes','total eve minutes','total night minutes']
data.groupby(['churn'])[columnsgrp].agg(np.mean)

#can use this method shortly show selected data we want in group

# Additional Visualizations Inline for VS Code Interactive Window
plt.figure(figsize=(10,5))
sb.boxplot(x='churn', y='total day minutes', data=data)
plt.title('Total Day Minutes by Churn')
plt.show()

plt.figure(figsize=(10,5))
sb.boxplot(x='churn', y='total eve minutes', data=data)
plt.title('Total Eve Minutes by Churn')
plt.show()

plt.figure(figsize=(10,5))
sb.boxplot(x='churn', y='total night minutes', data=data)
plt.title('Total Night Minutes by Churn')
plt.show()
