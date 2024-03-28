import pandas as pd

df = pd.read_csv('data.csv', sep=',')
df = df[df['Continent'] == 'South America']
print(df)
'''
countries = df['Country'].values
percentages = df['World Population Percentage'].values

'''
