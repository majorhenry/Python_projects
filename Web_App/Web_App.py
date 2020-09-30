import folium
import pandas


data = pandas.read_csv('Volcanoes_USA.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

def color_producer(elevation):
    if elevation < 1600:
        return 'green'
    elif 1600<= elevation < 2800:
        return "oramge"
    else:
        return "red"

map=folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")

fg_v = folium.FeatureGroup(name='Volcanoes_USA')

for lt, ln, el in zip(lat, lon, elev):
    fg_v.add_child(folium.CircleMarker(location=[lt, ln],radius = 9, popup=str(el)+"m",
    fill_color=color_producer(el), color='grey', fill=True, fill_opacity=0.7))
    # icon=folium.Icon(colour=color_producer(el))))  #You may get a blank webpage if there are quotes('')in the string. to avoid that change the popup argument to:
    #popup=folium.Popup(str(el),parse_)html=True #however, for simple string like elevation values this is not a problem since there are no quotes in them.

fg_p = folium.FeatureGroup(name='Population')

fg_p.add_child(folium.GeoJson(data=open("115 world.json", 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
#fg.add_child(folium.GeoJson(data=(open("115 world.json", 'r', encoding='utf-8-sig').read(),)))


map.add_child(fg_v)
map.add_child(fg_p)

map.add_child(folium.LayerControl())

map.save("Map2.html")
