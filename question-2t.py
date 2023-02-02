#Question 2:

#Libraries required
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#Import the given “Salary_Data.csv” 
train_test = pd.read_csv('C:/Users/namra/Downloads/Salary_Data.csv')
#Dividing the dataframes
X = train_test.iloc[:, 0:1].values
y = train_test.iloc[:, 1].values
# Dividing data into two dataframes in a way that test datea is 1/3rd of original data
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 1/3, random_state = 0)
# Performing linear regression on train dataframe
model = LinearRegression()
model.fit(X_train, y_train)
# Predicting the Test set results
y_pred = model.predict(X_test)
print(y_pred)
# Visualising the Training set results
plt.scatter(X_train, y_train, color = 'yellow')
plt.plot(X_train, model.predict(X_train), color = 'green')
plt.title('Salary VS Experience (Training set)')
plt.xlabel('Total years of experience')
plt.ylabel('Salary')
plt.show()
# Visualising the Test set results
plt.scatter(X_test, y_test, color = 'yellow')
plt.plot(X_train, model.predict(X_train), color = 'green')
plt.title('Salary VS Experience (Test set)')
plt.xlabel('Total years of experience')
plt.ylabel('Salary')
plt.show()
