#   ___                    ____           _           _
#  / _ \ _ __   ___ _ __  / ___|   _ _ __| |__   ___ | |_
# | | | | '_ \ / _ \ '_ \| |  | | | | '__| '_ \ / _ \| __|
# | |_| | |_) |  __/ | | | |__| |_| | |  | |_) | (_) | |_
#  \___/| .__/ \___|_| |_|\____\__,_|_|  |_.__/ \___/ \__|
#       |_|

# Сделать send_notification в 12:00 по мск
# Сделать нормальный start reaction


import telebot

import requests
import pandas as pd

import yfinance as yf

from datetime import datetime, timedelta





# @bot.message_handler(commands=['start'])
# def start_message(message):
# 	start_date = datetime.now() - timedelta(days=10)
# 	end_date = datetime.now()

# 	historical_exchange_rates = get_historical_exchange_rates(start_date, end_date)

# 	if historical_exchange_rates:
# 	    df = pd.DataFrame(historical_exchange_rates)

# 	    msg = df.to_string(index=False)
# 	    bot.send_message(message.chat.id, f"{msg}\n\nOpenCurbot")
# 	else:
# 	    bot.send_message(message.chat.id, "Ведутся техработы!\n\nOpenCurbot")


# @bot.message_handler(commands=["price"])
# def send_price(message):
# 	exchange_rate = get_exchange_rate()

# 	if exchange_rate:
# 	    df = pd.DataFrame(exchange_rate)

# 	    msg = df.to_string(index=False)
# 	    bot.send_message(message.chat.id, f"{msg}\n\nOpenCurbot")
# 	else:
# 	    bot.send_message(message.chat.id, "Ведутся техработы!\n\nOpenCurbot")


# @bot.message_handler(commands=["prices"])
# def send_prices(message):
# 	start_date = datetime.now() - timedelta(days=10)
# 	end_date = datetime.now()

# 	historical_exchange_rates = get_historical_exchange_rates(start_date, end_date)

# 	if historical_exchange_rates:
# 	    df = pd.DataFrame(historical_exchange_rates)

# 	    msg = df.to_string(index=False)
# 	    bot.send_message(message.chat.id, f"{msg}\n\nOpenCurbot")
# 	else:
# 	    bot.send_message(message.chat.id, "Ведутся техработы!\n\nOpenCurbot")


# bot.infinity_polling()
