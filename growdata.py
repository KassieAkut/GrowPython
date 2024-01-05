import pandas as pd
import plotly.express as px
import plotly.offline as pyo

# Read the dataset into a dataframe
read_file = 'C:/Users/kassi/Desktop/Grow/Growlocations.csv'
df = pd.read_csv(read_file)

# Filter data based on bounding box
df_range = df[
    (df['Longitude'] >= -10.592) & (df['Longitude'] <= 1.6848) &
    (df['Latitude'] >= 50.681) & (df['Latitude'] <= 57.985)
]
# Print a few rows to inspect the data
print(df_range.head())

# Create map using Plotly Express
fig = px.scatter_mapbox(
    df_range,
    lat='Latitude',
    lon='Longitude',
    zoom=5,
)

# Set the Mapbox style
fig.update_layout(mapbox_style="open-street-map")

# Show the map
fig.show(renderer='browser')
pyo.plot(fig, filename='map.html', auto_open=True)
