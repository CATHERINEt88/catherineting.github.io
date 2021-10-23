import pandas as pd
from pandas.io import html

df = pd.read_csv('Resources/cities.csv')

datahtml = df.to_html()
print(html)