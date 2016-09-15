"""
from django.test import TestCase

from models import Pais, Provincia
from views import SOAPService


class SOAPSeviceTestCase(TestCase):

    def setUp(self):
        Pais.objects.create(descripcion='Argentina', valor='ARG')
        Pais.objects.create(descripcion='Colombia', valor='COL')
        Pais.objects.create(descripcion='Alemania', valor='ALE')
        Pais.objects.create(descripcion='Italia', valor='ITA')

    def tearDown(self):
        Pais.objects.all().delete()

    def test_get_paises(self):
        soap_service = SOAPService()
        result = soap_service.get_paises()
        self.assertEqual(4, len(result))

    def test_get_pais(self):
        soap_service = SOAPService()
        result = soap_service.get_pais(3)
        self.assertEqual('Alemania', result.descripcion)

    def test_get_provincias_por_pais(self):

        pais = Pais.objects.get(pk=1)

        Provincia.objects.create(pais=pais, descripcion='Catamarca')
        Provincia.objects.create(pais=pais, descripcion='Corrientes')

        soap_service = SOAPService()
        result = soap_service.get_provincias_por_pais(1)

        self.assertEqual(2, len(result))
"""