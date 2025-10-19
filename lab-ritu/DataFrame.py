import pandas
import pandas as pd
df = pd.read_csv("iris.csv")
print(type(df))
print(df.head())
print(df.columns)
print(df.index)
print(df.iloc[1])
print(df.iloc[1,1])
X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width',
       'species']]
y = df['species']

