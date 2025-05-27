# app.py

import streamlit as st
import requests
import pandas as pd
import pydeck as pdk

# 설정
st.set_page_config(page_title="세계 대기오염 실시간 모니터링", layout="wide")
st.title("🌍 전 세계 대기오염 실시간 모니터링")

# API 토큰
API_TOKEN = "YOUR_WAQI_API_TOKEN"

# 도시 목록 예시 (필요에 따라 확장 가능)
cities = {
    "Seoul": "seoul",
    "Tokyo": "tokyo",
    "New York": "new york",
    "London": "london",
    "Paris": "paris",
    "Delhi": "delhi",
    "Beijing": "beijing"
}

selected_city = st.selectbox("도시 선택", list(cities.keys()))
city_query = cities[selected_city]

# API 호출
@st.cache_data(ttl=600)
def get_air_quality(city):
    url = f"https://api.waqi.info/feed/{city}/?token={API_TOKEN}"
    response = requests.get(url)
    if response.status_code == 200 and response.json()["status"] == "ok":
        data = response.json()["data"]
        return {
            "city": city,
            "aqi": data["aqi"],
            "dominentpol": data.get("dominentpol", "N/A"),
            "lat": data["city"]["geo"][0],
            "lon": data["city"]["geo"][1]
        }
    return None

data = get_air_quality(city_query)

if data:
    st.metric(label=f"{selected_city}의 AQI (대기질지수)", value=data["aqi"])
    st.write(f"주 오염물질: **{data['dominentpol']}**")
    
    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state=pdk.ViewState(
            latitude=data["lat"],
            longitude=data["lon"],
            zoom=10,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                "ScatterplotLayer",
                data=pd.DataFrame([data]),
                get_position="[lon, lat]",
                get_color="[255, 0, 0, 160]",
                get_radius=50000,
            ),
        ],
    ))
else:
    st.error("데이터를 불러오지 못했습니다. 도시 이름이나 API 상태를 확인해주세요.")
