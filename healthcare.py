import pandas as pd # imports pandas library and gives it the nickname pd
df = pd.read_csv('healthcare_dataset.csv') # load the healthcare csv file into Dataframe called df
print(df.head()) # print the first 5 rows to preview the data
print(df.columns) # print all column names in the dataset
print(df['Billing Amount'].mean()) # calculate and print the average billing amount
print(df['Medical Condition'].value_counts()) # count how many patient have each medical condition
print(df.groupby('Medical Condition')['Billing Amount'].mean().round(2)) # group by condtion and calculate average billing rounded to 2 decimals
print(df['Test Results'].value_counts()) # count how many patients have each results 
df.to_csv('healthcare_output.csv', index=False) # savethe Dataframe to a new csv file without row numbers
print('File saved') # confirmation message that the file was saved successfully