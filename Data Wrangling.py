
import numpy as np
import pandas as pd


#import the data
data = {'first_name':'Zen', 'Ken', 'Jad', 'Kan', 'Sam'],
        'last_name':['Ali', 'Rami', '', 'Karam', 'Amir'],
        'age':[42, 52, 36, 24, 73],
        'preTestScore':[4, 24, 31, '', ''], 
        'postTestScore':['25,000', '94,000', 57, 62, 70]}

#put the data in a dataframe
df = pd.DataFrame(data)
print(df)

#Save the data frame into a .csv file as project.csv
df.to_csv("C:/Users/ASUS/Desktop/25sep.csv")

#Read the project.csv file and print the data frame
df = pd.read_csv("C:/Users/ASUS/Desktop/25sep.csv")
print (df)

#Read the project.csv file without column heading
df = pd.read_csv("C:/Users/ASUS/Desktop/25sep.csv", header = None)
print (df)

#Read the project.csv file and make two index columns, namely, ‘First Name’ and ‘Last Name’
df = pd.read_csv("C:/Users/ASUS/Desktop/25sep.csv", usecols= ['first_name', 'last_name'])
print (df)

#Print the data frame in a Boolean form as True or False. True for Null/ NaN values and false for non-null values
df = pd.read_csv('C:/Users/ASUS/Desktop/25sep.csv', na_values=['.'])
print(pd.isnull(df))

#Read the data frame by skipping the first 3 rows and print the data frame
df = pd.read_csv('C:/Users/ASUS/Desktop/25sep.csv', skiprows=3)
print(df)
