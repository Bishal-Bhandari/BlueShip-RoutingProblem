import plotly.express as px
import pandas as pd

x = px.data.carshare()
df = x.head(10)
print(df)

fig = px.scatter_mapbox(df,
                        lon=df['centroid_lon'],
                        lat=df['centroid_lat'],
                        zoom=3,
                        color=df['peak_hour'],
                        size=df['car_hours'],
                        width=1200,
                        height=900,
                        title='Blue Ship Routing')
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r": 0, "t": 50, "l": 0, "b": 10})

fig.show()
print("Plot.....")

