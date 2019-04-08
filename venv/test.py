import time
import pprint
import threading
from bitmex_websocket import BitMEXWebsocket
import matplotlib; matplotlib.use("TkAgg")
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
#from collections import OrderedDict,defaultdict
import pandas as pd
from bitmex import bitmex
import json, requests
import winsound
#///////////
import random

class Algorithm(object):

    def __init__(self,value_pair):
        global Flag_of_begining
        Flag_of_begining=False
        api_key = '6AnZMBW9F-a2Yf1cH28v_l8j'
        self.value_pair=value_pair
        self.Flag_of_begining = False
        secret_key = 'JsFkkeg2AMQziEsWioNmQzGm9LDNS5310NkXAT1FRxZdpu6k'
        self.ws=BitMEXWebsocket(endpoint="https://testnet.bitmex.com/api/v1", symbol=f'{self.value_pair}', api_key=api_key, api_secret=secret_key)
        self.ws.get_instrument()
        self.counter=0
        self.shoulder = 50
        self.start_money = 10

        pass
    def currancy_value(self,count=1):
        start_time=time.time()
        time.sleep(1.05)
        price_response=self.ws.get_ticker()
        #print(self.counter,'    ',price_response['last'])
        self.counter+=1
        return (time.time()-start_time),price_response['last'],
    def currancy_value1(self,value='XBT',count=1):
        start_time=time.time()
        time.sleep(2.05)
        price_response = requests.get(
            f'https://testnet.bitmex.com/api/v1/trade?symbol={value}&filter=%7B%22side%22%3A%22Sell%22%7D&count={count}&reverse=true').json()
        return (time.time()-start_time),price_response[0]['price'],
    def first_proizvod(self,mass,time):
        return (mass[-1]-mass[-2])/(time[-1]-time[-2])

    def second_proizvod(self,mass,time):
        buf=((mass[-1]-mass[-2])/(time[-1]-time[-2])-(mass[-2]-mass[-3])/(time[-2]-time[-3]))/\
            (time[-1]-time[-3])
        return buf
    def dt(self,mas):
        return mas[-1]-mas[-2]

    def analysis(self):

        iteracia=0
        Flag=False

        f = open(f'calculation_{self.value_pair}.txt', 'w')
        f.write('итерация  цена                     dt                         первая производная     вторая производная \n')
        f1=open('analysis.txt', 'w')
        f1.write('первая производная            вторая производная           доход в $     доход в процентах %        плечо      \n')
        time,price = self.currancy_value()
        self.price_mas, self.time_mas = [price] , [0]
        while True:
            if iteracia>10:
                self.Flag_of_begining=True
            print(iteracia+1)
            time,price=self.currancy_value()
            self.price_mas.append(price)

            self.time_mas.append(time+self.time_mas[-1])
            #print(self.price_mas,self.time_mas)
            if len(self.price_mas)>1:
                try:
                    first_proizvod_mas
                except:
                    first_proizvod_mas = [self.first_proizvod(self.price_mas, self.time_mas)]

                else:
                    first_proizvod_mas.append(self.first_proizvod(self.price_mas,self.time_mas))
                    if abs(first_proizvod_mas[-1])>0:
                        print('первая производная = ',first_proizvod_mas[-1])
                    #print('dt',self.time_mas[-1]-self.time_mas[-2])

                    if len(first_proizvod_mas)>1:

                        try:
                            second_proizvod_mas
                        except:
                            second_proizvod_mas = [self.second_proizvod(self.price_mas, self.time_mas)]

                        else:
                            second_proizvod_mas.append(self.second_proizvod(self.price_mas, self.time_mas))
                            if abs(first_proizvod_mas[-1])>0:
                                print('вторая производная = ',second_proizvod_mas[-1])

#            begining of analysis' calculatios with 1st and 2nd derivative

            if len(self.price_mas)>5:
                if first_proizvod_mas[-1]>0 and first_proizvod_mas[-2]>0 and first_proizvod_mas[-3]>0:
                    if second_proizvod_mas[-1]>0 and second_proizvod_mas[-2]>0:
                        print('!!!!!!!!!!!!')
                        winsound.MessageBeep()
                        winsound.MessageBeep()
                        purchase_price=self.price_mas[-1]
                        flag_purchase=True
            '''if Flag:
                if first_proizvod_mas[-1]<0:
                    profit_L=(self.price_mas[-1]-purchase_price)/purchase_price
                    f1.write(f'{first_proizvod_mas[-4]}        ----        -------     --------    {self.shoulder} \n')
                    f1.write(f'{first_proizvod_mas[-3]}        {second_proizvod_mas[-3]}        -------     --------    {self.shoulder} \n')
                    f1.write(f'{first_proizvod_mas[-2]}        {second_proizvod_mas[-2]}        -------     --------    {self.shoulder} \n')
                    f1.write(f'{first_proizvod_mas[-1]}        {second_proizvod_mas[-1]}        {(1+profit_L)*self.start_money}     {profit_L*100}    {self.shoulder} \n')
                    f.close()
                    f1.close()
                    winsound.MessageBeep()
                    winsound.MessageBeep()
                    winsound.MessageBeep()
                    exit()'''
            if iteracia>2:
                f.write(f'{iteracia}         {self.price_mas[-1]}                  {self.dt(self.time_mas)}          {first_proizvod_mas[-1]}                     {second_proizvod_mas[-1]} \n')
            if iteracia==500:
                f.close()
                exit()
            iteracia+=1

            if (iteracia%500)==0:
                print('очистка массивов')
                buf_1=first_proizvod_mas[-10:]
                buf_2=second_proizvod_mas[-10:]
                buf_p = self.price_mas[-10:]
                buf_t = self.time_mas[-10:]
                first_proizvod_mas= buf_1
                second_proizvod_mas=buf_2
                self.price_mas=buf_p
                self.time_mas=buf_t



class Grafic(Algorithm):
    def __init__(self):

        #self.Flag_of_beginingG =Algorithm.Flag_of_begining
        #print(self.Flag_of_beginingG)
        pass

    def _graph(self):
        #print('Grafic   ',self.Flag_of_beginingG)
        while not Flag_of_begining:
            time.sleep(2)
            print(Flag_of_begining)
            if Flag_of_begining:
                print(Flag_of_begining)
            pass
        if Flag_of_begining:
            # First set up the figure, the axis, and the plot element we want to animate
            fig = plt.figure()
            print('///////////////')
            ax = plt.axes(xlim=(0, 100), ylim=(5100, 5200))
            self.line, = ax.plot([], [], lw=2)
            #print(line, )
            self.x_data, self.y_data = self.time_mas,self.price_mas
            anim = animation.FuncAnimation(fig, self.animate, init_func=self.init1,frames=50, interval=100,repeat=False, blit=False)


            plt.show()

    # initialization function: plot the background of each frame
    def init1(self):
        self.line.set_data([], [])
        print((self.line,))
        return (self.line,)

    # animation function.  This is called sequentially
    def animate(self,i):
        Flag=False
        i = random.randint(0, 5)
        time.sleep(1.2)
        if len(self.x_data)>10 or Flag == True:
            Flag=True
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
A=Algorithm('XBTJPY')

Graf = Grafic()
print('//////',Flag_of_begining)
t = threading.Thread(target=Graf._graph(),daemon=True)
t1 = threading.Thread(target=A.analysis(),daemon=True)
#A.analysis()
print('???????')
t.start()
t1.start()


t.join()

