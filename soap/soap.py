# -*- coding: utf-8 -*-

from suds.client import Client

url = 'http://45.55.78.45/soap/wsdl'
client1 = Client(url, cache=None)
#client1.service.say_hello("Dave",5)

result = client1.service.EjemploDeMetodo(6)

print result