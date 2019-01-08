import folium
import csv


latitude = []
longitude = []
capacity = []

# def read_file():
f = open('./parking_area.csv', mode='r')

line = csv.reader(f, delimiter=',')
for i in line:
    print(i)
    longitude.append(i[40])
    latitude.append(i[39])
    capacity.append(i[10])

f.close()


latitude.pop(0)
longitude.pop(0)
capacity.pop(0)
# olium.Marker([lat, lon], popup=str(name)+': '+color+'-'+str(clname), icon=folium.Icon(color=color)).add_to(feature_group

map_osm = folium.Map(location=[37.5344578, 126.9861439], zoom_start=12)

for i in range(14000, len(latitude)):
    if int(capacity[i]) >= 50:
        folium.Marker([float(latitude[i]), float(longitude[i])], popup=capacity[i], icon=folium.Icon(color = 'red' if int(capacity[i]) > 100
                                                                                                            else 'green')).add_to(map_osm)


map_osm.save('./parking_area3.html')


#
# if __name__ == '__main__':
#     read_file()
