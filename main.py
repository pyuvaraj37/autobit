from pandas import DataFrame
import matplotlib.pyplot as plt
import robin_stocks as r 
import tkinter as t
from bit import Bit

#main
# login = r.login('yrenter@gmail.com','1y6a8s1w3a1n')

b = Bit('yrenter@gmail.com','1y6a8s1w3a1n')
b.set_historical_window(5)
btc_ma = b.get_moving_average()
print(btc_ma)

# btc_history = r.crypto.get_crypto_historicals('BTC','5minute', 'day', '24_7')
# interval = btc_history['data_points']
# last50min = interval[276:287]
# data_point_close_price = []
# for data_point in last50min:
#     print(data_point)

# Data = {
#     'Times' : [-50, -45, -40, -35, -30, -25, -20, -15, -10, -5, 0],
#     'Value' : data_point_close_price
# }

# df = DataFrame(Data,columns=['Times','Value'])
# df.plot(x ='Times', y='Value', kind = 'line')
# plt.show()

# root = t.Tk() 
# menu = t.Menu(root) 
# root.config(menu=menu) 
# filemenu = t.Menu(menu) 
# menu.add_cascade(label='Intervals', menu=filemenu) 
# filemenu.add_command(label='1 minute', command=) 
# filemenu.add_command(label='5 minute') 
# filemenu.add_separator() 
# filemenu.add_command(label='Exit', command=root.quit) 
# helpmenu = t.Menu(menu) 
# menu.add_cascade(label='Help', menu=helpmenu) 
# helpmenu.add_command(label='About') 
# t.mainloop() 
