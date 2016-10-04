
from datetime import datetime

from django.http import HttpResponse

from soaplib.core import Application
from soaplib.core.model.clazz import Array, ClassModel
from soaplib.core.model.primitive import (Boolean, DateTime, Double, Integer,
                                          String)
from soaplib.core.server.wsgi import Application as WSGIApplication
from soaplib.core.service import DefinitionBase, soap

import models


class SoapCredentials(ClassModel):
    Cliente = String
    Password = String


class ExtensionDataObject(ClassModel):
    SoapCredentials = SoapCredentials


class TargetInfo(ClassModel):
    ExtensionData = ExtensionDataObject
    Codigo = Integer
    Descripcion = String
    Tipo = Integer


class TargetRatingsInfo(ClassModel):
    TargetInfo1 = TargetInfo
    RatingPorc = Double
    RatingMiles = Double


class ArrayOfTargetRatingsInfo(ClassModel):
    TargetRatingsInfo = TargetRatingsInfo


class EvaluacionSpotInfoCompletaPorProdAnunciante(ClassModel):
    Region = Integer
    Fecha = DateTime
    Minuto = DateTime
    CodigoTema = Integer
    Tema = String
    Duracion = Integer
    Canal = Integer
    Anunciante = String
    Producto = String
    CodigoMaterial = Integer
    Material = String
    LTargetRatingsInfo = ArrayOfTargetRatingsInfo


class ArrayOfEvaluacionSpotInfoCompletaPorProdAnunciante(ClassModel):
    EvaluacionSpotInfoCompletaPorProdAnunciante = Array(
                            EvaluacionSpotInfoCompletaPorProdAnunciante)


class SOAPService(DefinitionBase):

    __tns__ = '[url]http://12.0.0.1:8000/soap/wsdl[/url]'

    __in_header__ = SoapCredentials

    @soap(String, String, String, String,
          _returns=ArrayOfEvaluacionSpotInfoCompletaPorProdAnunciante)
    def SpotsPorProductosAnunciante(
            self, codigo_Plaza, codigo_Vehiculo, fechaDesde, fechaHasta):

        array_result = ArrayOfEvaluacionSpotInfoCompletaPorProdAnunciante()

        array_result.EvaluacionSpotInfoCompletaPorProdAnunciante = []

        if self.ValidaUsuario(self.in_header):

            emisiones = models.Emision.objects.all()

            for emision in emisiones:

                fecha = datetime.strptime(str(emision.fecha), '%Y-%m-%d')
                hora = datetime.strptime(str(emision.hora), '%H:%M:%S')

                evaluacion_spot = EvaluacionSpotInfoCompletaPorProdAnunciante()
                evaluacion_spot.Region = 1
                evaluacion_spot.Fecha = fecha
                evaluacion_spot.Minuto = hora
                evaluacion_spot.CodigoTema = emision.id
                evaluacion_spot.Tema = emision.titulo
                evaluacion_spot.Duracion = emision.duracion
                evaluacion_spot.Canal = 1
                evaluacion_spot.Anunciante = emision.anunciantes.nombre
                evaluacion_spot.Producto = emision.producto.nombre
                evaluacion_spot.CodigoMaterial = emision.tipo_publicidad.id
                evaluacion_spot.Material = "material"
                evaluacion_spot.LTargetRatingsInfo = 0

                array_result.EvaluacionSpotInfoCompletaPorProdAnunciante.append(
                    evaluacion_spot)

        return array_result

    @soap(SoapCredentials, _returns=Boolean)
    def ValidaUsuario(self, s):
        if s.Cliente == "usuario1" and s.Password == "123456":
            return True
        return False


class DjangoSoapApp(WSGIApplication):

    csrf_exempt = True

    def __init__(self, services, tns):
        return super(DjangoSoapApp,
            self).__init__(Application(services, tns))

    def __call__(self, request):
        django_response = HttpResponse()

        def start_response(status, headers):
            django_response.status_code = int(status.split(' ', 1)[0])
            for header, value in headers:
                django_response[header] = value

        response = super(DjangoSoapApp, self).__call__(request.META,
            start_response)
        django_response.content = '\n'.join(response)

        return django_response

my_soap_service = DjangoSoapApp([SOAPService], __name__)