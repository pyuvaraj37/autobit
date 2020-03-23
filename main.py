import json
import robin_stocks as r 


#main
login = r.login('yrenter@gmail.com','1y6a8s1w3a1n')
usr_stocks = r.build_holdings()
btc_history = r.crypto.get_crypto_history('BTC','day', 'year', '24_7')

for key, value in btc_history.items():
    if key != 'data_points':
        print(key, value)
    else: 
        print(value[0])



