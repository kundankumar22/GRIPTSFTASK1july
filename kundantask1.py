# -*- coding: utf-8 -*-
"""kundantask1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VUpCjR30Ry2zIfxWyTeRPttorQ0pR5Gp

# **GRIP The Spark Foundation- Data Science & Business Analytics Internship**
**Author - Kundankumar Rahangdale**

**Task 1**: Prediction using Supervised ML

##**Aim: To predict the percentage of a student based on the no. of study hours**.
"""

# Commented out IPython magic to ensure Python compatibility.
#Importing Libraries required for data analysis
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt  
# %matplotlib inline
plt.style.use("ggplot")

#Reading the data from Dataset
dataset = "http://bit.ly/w-data"
student_data = pd.read_csv(dataset)
print("Data imported successfully")
student_data.head(10) #if no number is written then it will display first 5 headings

student_data.tail(10)

#To identify the number of rows and columns of the data
student_data.shape

#Size of dataframe which is calculated by number of rows and columns
student_data.size

#Summary Of Statistics
student_data.describe()

student_data.dtypes

#to find correlation
student_data.corr()

# Plotting the graph for distribution of scores
student_data.plot(x='Hours', y='Scores',style='o')
plt.xlabel('Hours Studied')  
plt.ylabel('Percentage Score') 
plt.title('Percentage Vs. Hours Studied')  
plt.show()

"""It is evident from the graph that there is a positive linear relation between the number of hours studied and percentage of score

#**Preparing the data**
"""

X = student_data.iloc[:, :-1].values  
y = student_data.iloc[:, 1].values

from sklearn.model_selection import train_test_split  
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                            test_size=0.2, random_state=0)

"""
# **Training the Algorithm**"""

#training the data
from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(X_train, y_train) 

print("The data has been trained")

# Plotting the regression line
regression_line = regressor.coef_*X+regressor.intercept_

# Plotting for the test data
plt.scatter(X, y)
plt.plot(X, regression_line);
plt.xlabel('Hours Studied')  
plt.ylabel('Percentage Score') 
plt.title('Percentage Vs. Hours Studied') 
plt.show()

"""
# **Making Predictions**"""

print(X_test) # Testing data - In Hours
y_pred = regressor.predict(X_test) # Predicting the scores

# Comparing Actual vs Predicted Score
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})  
df

"""**To find Predicted Score if student studies 9.25 hours a day**"""

# Predicted Score for a student who studies for 9.25 hrs/ day
df = np.array(9.25)
df = df.reshape(-1, 1)
pred = regressor.predict(df)
print("If the student studies for 9.25 hours/day, the score is {}.".format(pred))

"""# **Evaluating the model**"""

from sklearn import metrics  
print('Mean Absolute Error:', 
      metrics.mean_absolute_error(y_test, y_pred))