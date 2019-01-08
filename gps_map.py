import folium
import pymysql

conn = pymysql.connect(host='192.168.30.124', user='root', password='123', db='image_test', charset='utf8')
curs = conn.cursor()

# SQL문 실행
curs.execute("select latitude, longitude from reco_img")

# 데이타 Fetch
gps = curs.fetchall()
print(gps)  # 전체 rows
print(len(gps))

map_osm = folium.Map(location=[gps[0][0], gps[0][1]], zoom_start=17)
for i in range(len(gps)):
    folium.Marker([gps[i][0], gps[i][1]], popup='촬영장소').add_to(map_osm)

map_osm.save('./my_map.html')

# Connection 닫기
conn.close()
