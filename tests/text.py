# Import required modules
import json
import pandas as pd

from datetime import date, datetime, timedelta
from moeximporter import MoexImporter, MoexSecurity, MoexCandlePeriods

# mi = MoexImporter()

# seclist = mi.getSecuritiesAllTraded()


# # Create an object to access ISS API requests
# mi = MoexImporter()
#
# seclist = mi.getSecuritiesAllTraded()
#
# # Create an object to access sequirity data
# sec = MoexSecurity('GAZP', mi)
#
# # Print information about security
# print(sec)
#
#
# # Request quotes as a pandas DataFrame
# quotes_df = sec.getHistoryQuotesAsDataFrame(date(2024, 7, 9), date(2024, 7, 10))
#
# # Request quotes as an array of dicts
# quotes_arr = sec.getHistoryQuotesAsArray(date(2023, 5, 1), date(2023, 9, 20))
#
# # Request candles as a pandas DataFrame
# candles_df = sec.getCandleQuotesAsDataFrame(date(2023, 5, 1), date(2023, 9, 20), interval=MoexCandlePeriods.Period1Hour)
#
# # Request candles as an array of dicts
# candles_arr = sec.getCandleQuotesAsArray(date(2023, 5, 1), date(2023, 9, 20), interval=MoexCandlePeriods.Period1Hour)
#
# print(quotes_df)
# print(quotes_df["LOW"])


#

#
# with open("stock_list.json", "r") as file:
#     json_stocks_list = json.load(file)
# df = pd.DataFrame(json_stocks_list)
# print(df)


# def get_moex_stocks_list():
#     try:
#         with open("stocks_list.json", "r") as file:
#             json_stocks_list = json.load(file)
#         return json_stocks_list

#     except FileNotFoundError:
#         stocks_list = []

#         for s in seclist:
#             if s["secid"].isupper():
#                 stocks_list.append({"secid": s["secid"], "shortname": s["shortname"], "is_traded": s["is_traded"]})

#         with open("stocks_list.json", "w") as file:
#             json.dump(stocks_list, file)

#         return stocks_list


# moex_stocks_list = get_moex_stocks_list()

# msg = pd.DataFrame(moex_stocks_list)
# print(msg["secid"][0])

# tick = MoexSecurity(msg["secid"][0], mi)
#
# print(tick)
#
# # Request quotes as a pandas DataFrame
# quotes_df = tick.getHistoryQuotesAsDataFrame(date(2024, 7, 5), date(2024, 7, 10))
#
# print(quotes_df[["HIGH", "LOW"]])


# def get_moex_tick_prices(ticket):
#     tick = MoexSecurity(ticket, mi)

#     today_time = datetime.now()

#     year = int(today_time.strftime('%Y'))
#     month = int(today_time.strftime('%m'))
#     day = int(today_time.strftime('%d'))

#     # Request quotes as a pandas DataFrame
#     quotes_df = tick.getHistoryQuotesAsDataFrame(date(year, month, day-10), date(year, month, day))

#     return f"{tick}\n{quotes_df[['HIGH', 'LOW']]}"


# print(get_moex_tick_prices(msg["secid"][0]))

# Проверка доступных для торгов тикетов
# with open("stocks_list.json", "r") as file:
#     json_stocks_list = json.load(file)
# stocks_list = pd.DataFrame(json_stocks_list)

# for i, s in enumerate(stocks_list["is_traded"]):
#     if s == 1:
#         print(stocks_list["secid"][i])
