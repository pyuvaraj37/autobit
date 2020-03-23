from pandas import DataFrame
import matplotlib.pyplot as plt
import robin_stocks as r 


#main
login = r.login('yrenter@gmail.com','1y6a8s1w3a1n')

btc_history = r.crypto.get_crypto_history('BTC','5minute', 'day', '24_7')
interval = btc_history['data_points']
last50min = interval[276:287]
data_point_close_price = []
for data_point in last50min:
    data_point_close_price.append(float(data_point['close_price']))

Data = {
    'Times' : [-50, -45, -40, -35, -30, -25, -20, -15, -10, -5, 0],
    'Value' : data_point_close_price
}

df = DataFrame(Data,columns=['Times','Value'])
df.plot(x ='Times', y='Value', kind = 'line')
plt.show()
