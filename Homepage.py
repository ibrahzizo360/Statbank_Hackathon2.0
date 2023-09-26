import streamlit as st

# st.title('Welcome')

from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/virgoaugustine/Ghana-GeoJSON-data/master/ghana_regions.json') as response:
    counties = json.load(response)
    
for k,v in counties.items():
    st.write(v)    

import pandas as pd

# df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
#                    dtype={"fips": str})
df = pd.read_csv('data.csv')
import plotly.express as px

fig = px.choropleth(df, geojson=counties, locations='Region', color='unemp',
                           color_continuous_scale="Viridis",
                           range_color=(0, 12),
                           scope="africa",
                           featureidkey="properties.region",
                           labels={'unemp':'Unemployment rate'}
                          )
fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

st.plotly_chart(fig)