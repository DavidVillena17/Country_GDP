import pandas as pd

df = pd.read_csv('/Users/DavidVillena/Documents/Personal/Proyectos/Mis proyectos/Country_GDP/data_gdp.csv')

#print(df.head(10))
print(df.info())

#print(df['Country Name'])#.unique())
print(df['2023'].max())
'''
df['Country Name'] = df['Country Name'].astype("string")

print(df['Country Name'].dtype)

df.to_csv('data_gdp.csv', index = False, encoding='utf-8' )

'''