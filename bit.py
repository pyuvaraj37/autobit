import robin_stocks as r

class Bit(object):
    username = ''
    password = ''
    interval = 0
    data = []

    def __init__(self,username, password):
        self.username = username
        self.password = password
    
    def set_historical_window(self, i):
        self.interval = i

    def get_moving_average(self):
        data = self.get_formated_historical()
        sum = 0
        for data_point in data:
            sum += float(data_point['close_price'])
        sum /= len(data)
        return sum

    #interval range 5 - 200 minute
    def get_formated_historical(self):
        interval = int(self.interval / 5)
        btc_history = self.get_historical()
        data = btc_history['data_points']
        if interval is 1:
            return data 
        interval_data = data[::interval]
        return interval_data

    def get_historical(self):
        login = r.login(self.username, self.password)
        btc_history = r.crypto.get_crypto_historical('BTC', '5minute', 'day', '24_7')
        login = r.logout(); 
        return btc_history

    def get_market_value(self):
        login = r.login(self.username, self.password)
        btc_info = r.get_crypto_quote('BTC')
        login = r.logout()
        return btc_info['mark_price']


