# Problem 1

def portfolio_intersection(stock_1, stock_2):
    common_stock = []

    # if 'either' stock is empty, return []

    if len(stock_1) == 0 or len(stock_2) == 0:
        return common_stock

    for stocks in stock_1:
        if stocks in stock_2 and stocks not in common_stock:
            common_stock.append(stocks)

    return common_stock

# stock_1 = ['ABSE', 'APPL', 'NVID', 'MSFT']
# stock_2 = ['MSFT', 'TSLA', 'XCOM', 'APPL']
# print(portfolio_intersection(stock_1, stock_2))

# Problem 2

def extract_stock_price(stock_data):
    data_parts = stock_data.split(';')

    for part in data_parts:
        if part.isdigit():
            return int(part)

    return 0

# stock_data = 'APPL;Trading above cap;180;SELL;do not short'
# price = extract_stock_price(stock_data)
# print(price)
# print(price + 10)

# Problem 3

def analyze_fund_description(description, target_length):  # target_length is basically the word limit

    if target_length < 0:
        return 0

    words = description.split()

    count = 0

    for word in words:
        if len(word) >= target_length:
            count = count + 1

    return count

# print (analyze_fund_description("MOON is the hottest and most splendiferous new cryptocurrency on the market do not delay in purchasing a googleplex of shares in it immediately", 5))

# Problem 4

def generate_trade_ticker(name):
    if name == '':
        print('No ticker can be generated without a stock name')
        return

    for letter in name:
        print(letter.upper(), end=' ')

# name = 'msft'
# generate_trade_ticker(name)

# Problem 5

def count_trade_frequency(data, symbol):
    words = data.split(';')
    count = 0

    if symbol == '' or data == '':
        return 0

    for word in words:

        word = word.strip()
        word = word.split()

        if word[0].lower() == symbol.lower():
            count = count + 1

    return count

# Some stocks have spaces, use strip method.

# print (count_trade_frequency('APPL BUY;MSFT BUY;MSFT SELL;TSLA SELL;APPL BUY; APPL SELL', 'appl'))
# print (count_trade_frequency('Appl BUY;Msft BUY;Msft SELL;TSLA SELL;Appl BUY; Appl SELL', 'MSFT'))
# print (count_trade_frequency('Appl BUY;Msft BUY;Msft SELL;TSLA SELL;Appl BUY; Appl SELL', ''))
# print (count_trade_frequency('', 'MSFT'))