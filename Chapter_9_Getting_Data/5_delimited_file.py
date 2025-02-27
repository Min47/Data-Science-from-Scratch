import csv

with open('tab_delimited_stock_prices.txt') as f:
    tab_reader = csv.reader(f, delimiter='\t')
    for row in tab_reader:
        date = row[0]
        symbol = row[1]
        closing_price = float(row[2])
        # process(date, symbol, closing_price)


# If file has headers:
# date:symbol:closing_price
# 6/20/2014:AAPL:90.91
# 6/20/2014:MSFT:41.68
# 6/20/2014:FB:64.5
# 6/19/2014:AAPL:91.86
with open('colon_delimited_stock_prices.txt') as f:
    colon_reader = csv.DictReader(f, delimiter=':')
    for dict_row in colon_reader:
        date = dict_row["date"]
        symbol = dict_row["symbol"]
        closing_price = float(dict_row["closing_price"])
        # process(date, symbol, closing_price)

# Even if the file don't have headers, you can pass them in:
# date:symbol:closing_price
with open('colon_delimited_stock_prices_no_headers.txt') as f:
    colon_reader = csv.DictReader(f, fieldnames=["date", "symbol", "closing_price"], delimiter=':')
    for dict_row in colon_reader:
        date = dict_row["date"]
        symbol = dict_row["symbol"]
        closing_price = float(dict_row["closing_price"])
        # process(date, symbol, closing_price)


# Writing out data:
todays_prices = {'AAPL': 90.91, 'MSFT': 41.68, 'FB': 64.5}

with open('comma_delimited_stock_prices.txt', 'w') as f:
    csv_writer = csv.writer(f, delimiter=',')
    for stock, price in todays_prices.items():
        csv_writer.writerow([stock, price])