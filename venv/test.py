import time
import pprint
import matplotlib; matplotlib.use("TkAgg")
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
#from collections import OrderedDict,defaultdict
import pandas as pd
from bitmex import bitmex
import json, requests
#///////////
import random

class Algorithm(object):
    def __init__(self):
        pass
    def currancy_value(self,value='XBT',count=1):
        start_time=time.time()
        time.sleep(2.2)
        price_response = requests.get(
            f'https://testnet.bitmex.com/api/v1/trade?symbol={value}&filter=%7B%22side%22%3A%22Sell%22%7D&count={count}&reverse=true').json()
        return (time.time()-start_time),price_response[0]['price'],
    def first_proizvod(self,mass,time):
        return (mass[-1]-mass[-2])/(time[-1]-time[-2])

    def second_proizvod(self,mass,time):
        buf=((mass[-1]-mass[-2])/(time[-1]-time[-2])-(mass[-2]-mass[-3])/(time[-2]-time[-3]))/\
            (time[-1]-time[-3])
        return buf

    def analysis(self):
        price, time = self.currancy_value()
        self.price_mas, self.time_mas = [price] , [0]
        while True:
            price,time=self.currancy_value()
            self.price_mas.append(price)
            self.time_mas.append(time+self.time_mas[-1])

            if len(self.price_mas)>1:
                try:
                    first_proizvod_mas
                except:
                    first_proizvod_mas = [self.first_proizvod(self.price_mas, self.time_mas)]

                else:
                    first_proizvod_mas.append(self.first_proizvod(self.price_mas,self.time_mas))
                    print('первая производная = ',first_proizvod_mas)

                    if len(first_proizvod_mas)>1:

                        try:
                            second_proizvod_mas
                        except:
                            second_proizvod_mas = [self.second_proizvod(self.price_mas, self.time_mas)]

                        else:
                            second_proizvod_mas.append(self.second_proizvod(self.price_mas, self.time_mas))
                            print('вторая производная = ',second_proizvod_mas)
class Grafic(Algorithm):
    def __init__(self):
        pass

    def _graph(self):
        # First set up the figure, the axis, and the plot element we want to animate
        fig = plt.figure()
        ax = plt.axes(xlim=(0, 100), ylim=(5100, 5200))
        self.line, = ax.plot([], [], lw=2)
        #print(line, )
        self.x_data, self.y_data = [0], [0]
        anim = animation.FuncAnimation(fig, self.animate, init_func=self.init1,frames=50, interval=100,repeat=False, blit=False)


        plt.show()

    # initialization function: plot the background of each frame
    def init1(self):
        self.line.set_data([], [])
        print((self.line,))
        return (self.line,)

    # animation function.  This is called sequentially
    def animate(self,i):
        i = random.randint(0, 5)
        if len(self.x_data)>10:
            a,b=self.x_data[-1],self.y_data[-1]
            self.x_data, self.y_data = [a], [b]
        '''self.x_data.append(i)
        self.y_data.append(i * i)'''
        x,y = (Algorithm.currancy_value())
        self.x_data.append(x+self.x_data[-1])
        self.y_data.append(y)
        #print(self.x_data, self.y_data)
        self.line.set_data(self.x_data, self.y_data)
        return self.line,

#buf=[i for i in price_response if i['side']=='Sell']
'''for i in price_response:
    if i['side']=='Sell':
        buf.update({'symbol':i['symbol'],'size':i['size'],'price':i['price']})'''
#print(buf)
'''api_key = "6AnZMBW9F-a2Yf1cH28v_l8j"
api_secret = "JsFkkeg2AMQziEsWioNmQzGm9LDNS5310NkXAT1FRxZdpu6k"

client = bitmex( test=True, config=None,api_key=api_key, api_secret=api_secret)
ohlcv_candles = pd.DataFrame(client.Trade.Trade_getBucketed(
            binSize='1m',
            symbol='XBTUSD',
            count=10,
            reverse=True
        ).result()[0])

asd=client.get_ticker(symbol='XBTUSD').result()
#client.bitmex.get_ticker(symbol=)'''
A=Algorithm()
A.analysis()

