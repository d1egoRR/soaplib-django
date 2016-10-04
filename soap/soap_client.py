# -*- coding: utf-8 -*-

from suds.client import Client

url = 'http://127.0.0.1:8000/soap/wsdl'
client1 = Client(url, cache=None)

credencial = client1.factory.create('SoapCredentials')

credencial.Cliente = "usuario1"
credencial.Password = "123456"


client1.set_options(soapheaders=credencial)


#result = client1.service.ValidaUsuario("nada")
result = client1.service.SpotsPorProductosAnunciante(
    "nada", "nada", "nada", "nada")

print result