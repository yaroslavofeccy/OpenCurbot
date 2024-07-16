# from tradingview_ta import TA_Handler, Interval, Exchange

# tesla = TA_Handler(
#     symbol="TSLA",
#     screener="america",
#     exchange="NASDAQ",
#     interval=Interval.INTERVAL_1_DAY
# )

# rub = TA_Handler(
#     symbol="USDRUB",
#     screener="forex",
#     exchange="FX_IDC",
#     interval=Interval.INTERVAL_1_DAY
# )
# print(tesla.get_analysis().summary)
# print(rub.get_analysis().summary)
# print(rub.get_analysis().screener)

# analis = analysis.indicators["open"]
# print(analis)
# # Example output: {"RECOMMENDATION": "BUY", "BUY": 8, "NEUTRAL": 6, "SELL": 3}

import pandas as pd
import yfinance as yf

def get_stock_data(symbol):
    stock = yf.Ticker(symbol)

    # Получение текущей стоимости акций
    price = stock.history(period='1d')['Close'][0]

    # Получение другой информации
    info = stock.info

    other_data = {
        'market_cap': info.get('marketCap', 'N/A'),
        'volume': info.get('volume', 'N/A'),
        'pe_ratio': info.get('trailingPE', 'N/A'),
        'dividend_yield': info.get('dividendYield', 'N/A')
    }

    return {
        'price': price,
        'other_data': other_data
    }

# Пример использования функции
symbol = "RUB=X"  # Символ акции Apple
data = get_stock_data(symbol)
print(data)
print(data["price"])


def get_historical_stock_info(tick: str):
    # Получаем данные по тикеру
    stock = yf.Ticker(tick)

    # Получаем исторические данные за последний месяц
    hist = stock.history(period="1mo")

    hist = hist[['High', 'Low']]
    hist.index = hist.index.date

    return hist


hhh = get_historical_stock_info("RUB=X")
print(hhh)
