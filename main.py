import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

# Read data file
df1 = pd.read_excel(r'SmallData.xlsx')
df2 = pd.read_excel(r'portpoint.xlsx')

# filter the data percentage to present
df1 = df1.sample(frac=0.25)

fig = go.Figure()
fig.add_trace(go.Scattergeo(
        lon=df1['Lon'],
        lat=df1['Lat'],
        hoverinfo='text',
        text=df1['Species_Type'],
        mode='markers',
        marker=dict(
            size=7,
            color='black',
        )))

for i in range(len(df2)):
    fig.add_trace(
        go.Scattergeo(
            lon=[df2['s_Lon'][i], df2['e_Lon'][i]],
            lat=[df2['s_Lat'][i], df2['e_Lat'][i]],
            mode='lines',
            line=dict(width=1, color='blue'),
        )
    )

fig.update_geos(fitbounds="locations")
fig.update_layout(
    title_text='Blue Ship Route<br>(Hover over the dots for species name)',
    showlegend=False,
    margin=dict(l=0, r=0, t=55, b=10),
    height=600,
    geo=dict(
        scope='world',
        showland=True,
        landcolor='lightgreen',
        showocean=True,
        oceancolor="lightBlue",
    ),
)

fig.show()
print("Plotting.....")
