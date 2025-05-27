import yfinance as yf
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# 글로벌 시총 10위 기업 티커 리스트
tickers = ['AAPL', 'MSFT', '2222.SR', 'GOOGL', 'AMZN', 'NVDA', 'BRK-B', 'TSLA', 'META', 'TSM']

# 데이터 다운로드 (최근 1년)
data = {}
for ticker in tickers:
    ticker_data = yf.Ticker(ticker)
    hist = ticker_data.history(period="1y")
    data[ticker] = hist['Close']

# plotly로 시각화
fig = go.Figure()

for ticker in tickers:
    fig.add_trace(go.Scatter(x=data[ticker].index, y=data[ticker], mode='lines', name=ticker))

fig.update_layout(
    title='글로벌 시총 10위 기업 주가 추이 (최근 1년)',
    xaxis_title='날짜',
    yaxis_title='종가 (USD)',
    hovermode='x unified'
)

fig.show()
