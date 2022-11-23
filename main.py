import plotly.express as px
import pandas as pd

# Read data file
df = pd.read_excel(r'SmallData.xlsx')

# filter the data percentage to present
df = df.sample(frac=0.5)

print(df)

fig = px.scatter_mapbox(df,
                        lon=df['Lon'],
                        lat=df['Lat'],
                        zoom=5,
                        color=df['Whale_Type'],
                        size=df['Population_Density'],
                        width=1200,
                        height=900,
                        title='Blue Ship Routing')
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r": 0, "t": 50, "l": 0, "b": 10})

fig.show()
print("Plotting.....")
