import pandas as pd # import pandas library and give it the nickname pd
df = pd.read_csv ('healthcare_dataset.csv') # open the healthcare dataset CSV file and load it into a DataFrame called df
emergency = df[df['Admission Type'] == 'Emergency'] # filter the dataset and keep only Emergency admission patients
print(emergency) # print all Emergency patients to the screen
print (emergency['Billing Amount'].mean()) # calculate and print the average billing amount for Emergency patients only
df['Age Group'] = pd.cut(df['Age'], bins = [0, 30, 60, 100],labels=['Young', 'Middle', 'Senior']) # create a new column that buckets patients into Young, Middle, and Senior age groups
print(df['Age Group'].value_counts()) # count how many patients fall into each age group
pivot = df.pivot_table(values='Billing Amount', index='Medical Condition', columns='Admission Type', aggfunc='mean').round(2) # build a table showing average billing for every combination of medical condition and admission type rounded to 2 decimals
print(pivot) # print the pivot table to the screen