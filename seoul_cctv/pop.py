import pandas as pd
#  import folium

ctx = '../data/'
xls = ctx+'population_in_Seoul.xls'
csv = ctx+'CCTV_in_Seoul.csv'

pop_data = pd.read_excel(xls)
cctv_data = pd.read_csv(csv)

print(cctv_data.head())
print(pop_data.head())

"""
m = folium.Map(location=[37, -102], zoom_start=5)
m.choropleth(
    geo_data = xls,
    name = 'choropleth',
    data = data,
    columns = ['State','population'],
    key_on = 'feature.id',
    fill_color = 'YlGn',
    fill_opacity=0.7,
    line_opacity = 0.2,
    legend_name = 'population Rate (%)'
)
folium.LayerControl().add_to(m)
"""