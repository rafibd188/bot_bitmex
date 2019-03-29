import hashlib
import json
import urllib
from collections import OrderedDict
import hmac
import httplib2
import requests
import time
import websocket
from bitmex_websocket import BitMEXWebsocket
#########################################################################################
server = 'testnet.bitmex.com'
api_key = 'v-4XB-7QQ_DKTdMA-gh4gWBg'
secret_key = 'aLAU5m5o86kSlk89K02HLcdGyf6uXizbHJ-RCooOmGRp41Bw'
#BITMEX_URL = "wss://testnet.bitmex.com"
BITMEX_URL = "wss://www.bitmex.com"

VERB = 'GET'
ENDPOINT = '/realtime'

#########################################################################################
class Client(object):
    SERVER = 'bitmex.com/api/v1'
    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key
        self.Parametrs = {}
    ##########################################################################################
    def _request_and_responce(self, method, **parametrs):
        self._conn().request \
                (
                method + '?' + parametrs['Currencypair'],
                self.Value,
                self.headers()
            )
        self.response = self.conn.getresponse()
        return self.response
    ##############################################################################################
    def _conn(self):
        self.conn = httplib2.HTTPSConnectionWithTimeout(self.SERVER)
        return self.conn
    ###########################################################################################
    def headers(self):
        return {"Api-key": self.api_key, "Sign": self.sign()}
    ##########################################################################################
    def sign(self):
        return new(self.secret_key.encode(), msg=self._Currency_pair().encode(),
                   digestmod=hashlib.sha256).hexdigest().upper()
    ############################################################################################
    def _Currency_pair(self):
        data = OrderedDict([(self.Currancypair, self.Value)])
        self.encoded_data = urllib.parse.urlencode(data)
        return self.encoded_data
    ###########################################################################################
    def _All_Tickers(self):
        self.Currancypair = ''
        self.Value = ''
        self._request_and_responce('/exchange/ticker', Type_of_request='GET', Currencypair=self._Currency_pair())
        return json.load(self.response)
    ###############################################################################################
    def _get_price(self, Value):
        self.Currancypair = 'currencyPair'
        self.Value = Value
        self._request_and_responce('/exchange/ticker', Type_of_request='GET', Currencypair=self._Currency_pair())
        return json.load(self.response)['last']

    ###############################################################################################
    def _OrderBook(self):
        self.Currancypair = ''
        self.Value ='XBT'
        self._request_and_responce('orderBook/L2', Type_of_request='', Currencypair=self._Currency_pair())
        return json.load(self.response)['last']
    ###############################################################################################
    def _Withdraw_fee(self, *spisok_value):
        data = []
        for i in self._Coin_info(*spisok_value):
            data.append(i['withdrawFee'])
        return data
    ##################################################################################################
    def _Coin_info(self, *spisok_value):
        self.Currancypair = ''
        self.Value = ''
        self._request_and_responce('/info/coinInfo', Type_of_request='GET', Currencypair='')
        data = json.load(self.response)['info']
        if len(spisok_value) != 0:
            buf = []
            for i in spisok_value:
                for j in range(len(data)):
                    if data[j]['symbol'] == i:
                        buf.append(data[j])
        else:
            return data
        return buf
def testadfs():
   ''' method = '/api/v1/orderBook/L2'
    value='XBT'
    depth=25
    #data = OrderedDict([('symbol', f'={value}&depth={depth}')])
    encoded_data='symbol'+f'={value}&depth={depth}'

    print(encoded_data)
    sign = new( secret_key.encode(), msg=encoded_data.encode(), digestmod=hashlib.sha256).hexdigest().upper()
    print(sign)
    headers = {"Api-key": api_key, "Sign": sign}
    print(headers)

    conn = httplib2.HTTPSConnectionWithTimeout(server)
    print(conn)
    conn.request('GET',method + '?' + encoded_data, '', headers)
    response = conn.getresponse().read().decode('utf-8')
    print(response)
    conn.close()
    value = json.loads(response)
    print('на счету ', value['value'], self.name)
    '''
   """Given an API Secret key and data, create a BitMEX-compatible signature."""
   data = ''
   if postdict:
       # separators remove spaces from json
       # BitMEX expects signatures from JSON built without spaces
       data = json.dumps(postdict, separators=(',', ':'))
   parsedURL = urllib.parse.urlparse(url)
   path = parsedURL.path
   if parsedURL.query:
       path = path + '?' + parsedURL.query
   # print("Computing HMAC: %s" % verb + path + str(nonce) + data)
   message = (verb + path + str(nonce) + data).encode('utf-8')
   print("Signing: %s" % str(message))

   signature = hmac.new(apiSecret.encode('utf-8'), message, digestmod=hashlib.sha256).hexdigest()
   print("Signature: %s" % signature)
   return signature
def prov():
    url='https://www.bitmex.com/api/v1'
    r=requests.get(url).content
    print(r)
def test_with_message():
    # This is up to you, most use microtime but you may have your own scheme so long as it's increasing
    # and doesn't repeat.
    expires = int(time.time()) + 5
    # See signature generation reference at https://www.bitmex.com/app/apiKeys
    signature = bitmex_signature(secret_key, VERB, ENDPOINT, expires)
    print(signature)
    # Initial connection - BitMEX sends a welcome message.
    ws = websocket.create_connection(BITMEX_URL + ENDPOINT)
    print("Receiving Welcome Message...")
    result = ws.recv()
    print("Received '%s'" % result)

    # Send API Key with signed message.
    request = {"op": "authKeyExpires", "args": [api_key, expires, signature]}
    ws.send(json.dumps(request))
    print('//////',json.dumps(request))
    print("Sent Auth request")
    result = ws.recv()
    print("Received '%s'" % result)

    # Send a request that requires authorization.
    request = {"op": "subscribe", "args": "position"}
    ws.send(json.dumps(request))
    print("Sent subscribe")
    result = ws.recv()
    print("Received '%s'" % result)
    result = ws.recv()
    print("Received '%s'" % result)

    ws.close()
def bitmex_signature(apiSecret, verb, url, nonce, postdict=None):
    """Given an API Secret key and data, create a BitMEX-compatible signature."""
    data = ''
    if postdict:
        # separators remove spaces from json
        # BitMEX expects signatures from JSON built without spaces
        data = json.dumps(postdict, separators=(',', ':'))
    parsedURL = urllib.parse.urlparse(url)
    path = parsedURL.path
    if parsedURL.query:
        path = path + '?' + parsedURL.query
    # print("Computing HMAC: %s" % verb + path + str(nonce) + data)
    message = (verb + path + str(nonce) + data).encode('utf-8')
    print("Signing: %s" % str(message))

    signature = hmac.new(apiSecret.encode('utf-8'), message, digestmod=hashlib.sha256).hexdigest()
    print("Signature: %s" % signature)
    return signature
def test():
    expires = int(time.time()) + 5
    # See signature generation reference at https://www.bitmex.com/app/apiKeys
    signature = bitmex_signature(secret_key, VERB, ENDPOINT, expires)
    print(signature)
    # Initial connection - BitMEX sends a welcome message.
    ws = websocket.create_connection(BITMEX_URL + ENDPOINT)
#test()
ws = BitMEXWebsocket(endpoint="https://testnet.bitmex.com/api/v1", symbol="XBTUSD", api_key=api_key, api_secret=secret_key)
ws.get_ticker()
