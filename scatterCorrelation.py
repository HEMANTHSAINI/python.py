import pandas as pd
import plotly.express as px

df = pd.read_csv("tv vs timespend.csv")
fig = px.scatter(df,x="Size of TV",y=" 	Average time spent watching TV in a week (hours)")
fig.show()
