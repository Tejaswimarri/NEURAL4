#Question 1:

#Libraries required
import pandas as pd
import matplotlib.pyplot as plt
#Reading the csv file into dataframe
data = pd.read_csv("C:/Users/namra/Downloads/data.csv")
#Printing top few rows
print(data.head())
data.describe()
#Printing top few rows
print(data.head())
data.describe()
#Replacing null values found with mean
data = data.fillna(data.mean())
#Select at least two columns and aggregate the data using: min, max, count, mean
print(data[['Maxpulse','Calories']].agg(['min','max','mean','count']))
#Filter the dataframe to select the rows with calories values between 500 and 1000.
print(data[(data.Calories < 1000) & (data.Calories > 500)])
#Filter the dataframe to select the rows with calories values > 500 and pulse < 100.
print(data[ (data.Calories>500) & (data.Pulse < 100)])
#Create a new “df_modified” dataframe that contains all the columns from df except for “Maxpulse”.
df_modified = pd.DataFrame(data, columns = ['Duration', 'Pulse', 'Calories'])
print (df_modified.head())
#Delete the “Maxpulse” column from the main df dataframe
del data["Maxpulse"]
print(data.head)
#Convert the datatype of Calories column to int datatype.
data['Calories'] = data['Calories'].astype("int")
print(data['Calories'].dtypes)
#Using pandas create a scatter plot for the two columns (Duration and Calories).
print(data.plot.scatter(x ='Duration', y= 'Calories'))
plt.show()





