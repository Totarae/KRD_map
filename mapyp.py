import folium
import pandas

data=pandas.read_csv("Stadion.csv")

lat=list(data["yandekskart_center_0"])
lon=list(data["yandekskart_center_1"])
titl=list(data["title"])
popul=list(data["population"])

def coloristic(populat):
    if populat<100:
        return 'red'
    elif 100<=populat<=4000:
        return 'orange'
    else:
        return 'green'

map=folium.Map(location=[45.02,38.97],zoom_start=12)

fgv=folium.FeatureGroup(name="Stadiums")

for lt, ln, tl, pl in zip(lat, lon, titl,popul):
    fgv.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(str(tl),parse_html=True), icon=folium.Icon(color=coloristic(pl))))

dta=pandas.read_csv("Sportp.csv", error_bad_lines=False)
lat1=list(dta["yandekskart_center_0"])
lon1=list(dta["yandekskart_center_1"])
fgs = folium.FeatureGroup(name="Sports")
for lt, ln in zip(lat1,lon1):
    fgs.add_child(folium.CircleMarker(location=[lt, ln], radius=4, fill_color='blue', color='grey', fill=True, fill_opacity=0.7))

gfj = folium.FeatureGroup(name="Dustricts")
gfj.add_child(folium.GeoJson(data=(open('map.geojson', 'r', encoding='utf-8-sig').read())))

map.add_child(fgv)
map.add_child(fgs)
map.add_child(gfj)
map.add_child(folium.LayerControl())

map.save("Map1.html")
