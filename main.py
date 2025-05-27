import streamlit as st
import streamlit as st
import folium
from streamlit_folium import st_folium

# 서초구 고등학교 데이터 (동덕여고 추가)
schools = [
    {"name": "서초고등학교", "lat": 37.4914, "lon": 127.0205},
    {"name": "경원고등학교", "lat": 37.4802, "lon": 127.0121},
    {"name": "세화고등학교", "lat": 37.4891, "lon": 127.0102},
    {"name": "경기고등학교", "lat": 37.4917, "lon": 127.0253},
    {"name": "동덕여자고등학교", "lat": 37.4827, "lon": 127.0140},  # 동덕여고 추가
]

st.title("서울시 서초구 고등학교 위치 지도 (동덕여고 포함)")

m = folium.Map(location=[37.4850, 127.0150], zoom_start=14)

for school in schools:
    folium.Marker(
        location=[school["lat"], school["lon"]],
        popup=school["name"],
        icon=folium.Icon(color='blue', icon='graduation-cap', prefix='fa')
    ).add_to(m)

st_folium(m, width=700, height=500)
