# -*- coding: utf-8 -*-

from suds.client import Client

url = 'http://127.0.0.1:8000/soap/wsdl'
client1 = Client(url, cache=None)
#client1.service.say_hello("Dave",5)

result = client1.service.EjemploDeMetodo(5)

print result