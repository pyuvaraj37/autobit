import tkinter as tk
from bit import Bit
import threading

class GUI(tk.Frame):

    bit = Bit('','')

    def __init__(self, username, password, master=None ):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.bit = Bit(username, password)

    def create_widgets(self):

        self.label = tk.Label(self)
        self.label["text"] = "AUTOBIT"
        self.label.grid(row=0, column=1)

        self.get_ma = tk.Button(self)
        self.get_ma["text"] = "Get Moving Average"
        self.get_ma["command"] = self.get_moving_average
        self.get_ma.grid(row=1, column=1)

        self.ma_value = tk.Text(self, height=1, width=10)
        self.ma_value.grid(row=1, column=2)

        self.ma = tk.Text(self, height=1, width=10)
        self.ma.grid(row=1, column=3)

        self.mp = tk.Text(self, height=1, width=10)
        self.mp.grid(row=1, column=4)
        
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.grid(row=1, column=5)


    def get_moving_average(self):
        print("Getting moving average...")
        value = self.retrieve_input()
        self.bit.set_historical_window(value)
        btc_ma = self.bit.get_moving_average()
        self.ma.insert(tk.END,str(btc_ma))

    def retrieve_input(self):
        input = self.ma_value.get("1.0", tk.END)
        return int(input)

    def get_market_value(self):
        input = self.bit.get_market_value()
        return input

    def update_market_price(self):
        print("Updating Market Price...")
        market_price = self.get_market_value()
        self.mp.insert(tk.END, market_price)
        self.mp.update(5000, self.update_market_price())
