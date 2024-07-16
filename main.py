#   ___                    ____           _           _
#  / _ \ _ __   ___ _ __  / ___|   _ _ __| |__   ___ | |_
# | | | | '_ \ / _ \ '_ \| |  | | | | '__| '_ \ / _ \| __|
# | |_| | |_) |  __/ | | | |__| |_| | |  | |_) | (_) | |_
#  \___/| .__/ \___|_| |_|\____\__,_|_|  |_.__/ \___/ \__|
#       |_|

# Сделать send_notification в 12:00 по мск
# Сделать нормальный start reaction
# Сделать нормальную базу данных


import telebot

import pandas as pd
from datetime import date, datetime, timedelta

import yfinance as yf

# Create bot object
bot = telebot.TeleBot("TOKEN")

# Open bot logo file
logo = open("logo.txt").readlines()

normal_logo = ""
for l in logo:
	l = l.replace("\n", "")
	normal_logo = normal_logo + l + "\n"

print(normal_logo)


def get_stock_data(symbol):
    stock = yf.Ticker(symbol)

    # Получение текущей стоимости акций
    price = stock.history(period='1d')['Close'][0]

    # Получаем дополненную информации
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


def get_historical_stock_info(tick: str, period: str):
    # Получаем данные по тикеру
    stock = yf.Ticker(tick)

    # Получаем исторические котировки (Open/Close)
    hist = stock.history(period=period)
    hist = hist[['Open', 'Close']]
    hist.index = hist.index.date

    # Разименовываем колонки для лучшего эстетического вида
    hist.columns = ['', '']
    return hist


@bot.message_handler(commands=['start'])
def start_message(message):
    try:
        historical_exchange_rates = get_historical_stock_info("RUB=X", "5d")

        msg = historical_exchange_rates
        bot.send_message(message.chat.id, f"Курс USD/RUB за последние 5 дней (Open/Close)\n\n{msg}\n\nOpenCurbot")
    except:
        bot.send_message(message.chat.id, "Ведутся техработы!\n\nOpenCurbot")


@bot.message_handler(commands=["price"])
def send_rt_usd_rub_price(message):
    try:
        exchange_rate = get_stock_data("RUB=X")

        msg = exchange_rate["price"]
        bot.send_message(message.chat.id, f"Курс USD/RUB на данный момент (YF)\n\n{msg}\n\nOpenCurbot")
    except:
        bot.send_message(message.chat.id, "Ведутся техработы!\n\nOpenCurbot")


@bot.message_handler(commands=["prices"])
def send_usd_rub_1M_prices(message):
    try:
        historical_exchange_rates = get_historical_stock_info("RUB=X", "1mo")

        msg = historical_exchange_rates
        bot.send_message(message.chat.id, f"Курс USD/RUB за последний месяц (Open/Close)\n\n{msg}\n\nOpenCurbot")
    except:
        bot.send_message(message.chat.id, "Ведутся техработы!\n\nOpenCurbot")


@bot.message_handler()
def send_ticket_prices(message):
    try:
        tick = str(message.text)
        if tick:
            historical_exchange = get_historical_stock_info(tick, "5d")

            msg = historical_exchange
            bot.send_message(message.chat.id, f"Курс {tick} за последние 5 дней (Open/Close)\n\n{msg}\n\nOpenCurbot")
    except:
        bot.send_message(message.chat.id, "Неверный тикет!\n\nOpenCurbot")


bot.infinity_polling()
