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

        self.winfo_toplevel().title("AUTOBIT")

        #Moving Average System

        #Interval Text Box, Value Text Box, and Button for 1
        self.ma_value_one = tk.Text(self, height=1, width=10)
        self.ma_value_one.grid(row=3, column=2)
        self.ma_interval_one = tk.Text(self, height=1, width=10)
        self.ma_interval_one.grid(row=3, column=1)
        self.get_ma_one = tk.Button(self)
        self.get_ma_one["text"] = "Get Moving Average"
        self.get_ma_one["command"] = lambda arg1=self.ma_value_one, arg2=self.ma_interval_one :self.get_moving_average(arg1,arg2)
        self.get_ma_one.grid(row=3, column=0)

        #Interval Text Box, Value Text Box, and Button for 2
        self.ma_value_two = tk.Text(self, height=1, width=10)
        self.ma_value_two.grid(row=4, column=2)
        self.ma_interval_two = tk.Text(self, height=1, width=10)
        self.ma_interval_two.grid(row=4, column=1)
        self.get_ma_two = tk.Button(self)
        self.get_ma_two["text"] = "Get Moving Average"
        self.get_ma_two["command"] = lambda arg1=self.ma_value_two, arg2=self.ma_interval_two :self.get_moving_average(arg1,arg2)
        self.get_ma_two.grid(row=4, column=0)

        #Text Box for Market Price
        self.mp = tk.Text(self, height=1, width=25)
        self.mp.insert(tk.END, "Getting Market Price...")
        self.master.after(10000, self.update_market_price)
        self.mp.grid(row=1, column=1)
        
        #Quit Button
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.grid(row=5, column=1)


    def get_moving_average(self, ma, ma_value):
        print("Getting moving average...")
        ma.delete("1.0",tk.END)
        value = int(self.retrieve_input_from_TB(ma_value))
        self.bit.set_historical_window(value)
        btc_ma = self.bit.get_moving_average()
        ma.insert(tk.END, btc_ma)

    def retrieve_input_from_TB(self, ma_value):
        input = ma_value.get("1.0", tk.END)
        return input

    def get_market_value(self):
        input = self.bit.get_market_value()
        return input

    def update_market_price(self):
        print("Updating Market Price...")
        self.mp.delete("1.0", tk.END)
        market_price = self.get_market_value()
        self.mp.insert(tk.END, market_price)
        self.master.after(60000,self.update_market_price)
        
