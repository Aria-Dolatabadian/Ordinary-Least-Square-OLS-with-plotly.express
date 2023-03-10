import plotly.express as px
import pandas as pd
df = pd.read_csv("Data.csv")
fig = px.scatter(
    df, x='total_bill', y='tip', opacity=0.65,
    trendline='ols', trendline_color_override='darkblue'
)
fig.show()
