import streamlit as st
import yfinance as yf
import plotly.graph_objs as go

st.title("글로벌 시총 10위 기업 주가 시각화")

tickers = ['AAPL', 'MSFT', '2222.SR', 'GOOGL', 'AMZN', 'NVDA', 'BRK-B', 'TSLA', 'META', 'TSM']

# 기간 선택 UI
period = st.selectbox("데이터 기간 선택", ["1mo", "3mo", "6mo", "1y"], index=3)

data = {}
for ticker in tickers:
    ticker_data = yf.Ticker(ticker)
    hist = ticker_data.history(period=period)
    data[ticker] = hist['Close']

fig = go.Figure()

for ticker in tickers:
    fig.add_trace(go.Scatter(x=data[ticker].index, y=data[ticker], mode='lines', name=ticker))

fig.update_layout(
    title=f'글로벌 시총 10위 기업 주가 추이 ({period})',
    xaxis_title='날짜',
    yaxis_title='종가 (USD)',
    hovermode='x unified'
)

st.plotly_chart(fig, use_container_width=True)
