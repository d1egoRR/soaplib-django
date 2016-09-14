
from soaplib.core.service import rpc, DefinitionBase, soap
from soaplib.core.model.primitive import String, Integer, Boolean, DateTime
from soaplib.core.model.clazz import Array
from soaplib.core import Application
from soaplib.core.server.wsgi import Application as WSGIApplication
from django.http import HttpResponse
from soaplib.core.model.clazz import ClassModel

import models


class PaisSerializer(ClassModel):

    __namespace__ = 'pais'
    descripcion = String
    valor = String


class HelloWorldService(DefinitionBase):

    __tns__ = '[url]http://12.0.0.1:8000/soap/wsdl[/url]'

    """
    @soap(String, Integer, _returns=Array(String))
    def say_hello(self, name, times):
        results = []
        for i in range(0, times):
            results.append('Hello, %s' % name)
        return results

    @soap(String, Integer, _returns=Array(String))
    def say_bye(self, name, times):
        results = []
        for i in range(0, times):
            results.append('Bye, %s' % name)
        return results
    """

    @soap(String, String, _returns=Array(String))
    def spots_por_productos_anunciante(self, codigo_plaza, codigo_vehiculo):
        return "def SpotsPorProductosAnunciante"

    @soap(Integer, DateTime, DateTime, Integer, String, Integer, Integer,
          String, String, Integer, String, String, _returns=Array(String))
    def EvaluacionSpotInfoCompletaPorProdAnunciante(self, Region, Fecha,
            Minuto, CodigoTema, Tema, Duracion, Canal, Anunciante, Producto,
            CodigoMaterial, Matrerial, LTargetRatingsInfo,
            _returns=Array(String)):
        return "def EvaluacionSpotInfoCompletaPorProdAnunciante"

    @soap(Integer, _returns=Integer)
    def EjemploDeMetodo(self, numero):
        return (10 * numero)

    @soap(_returns=Array(PaisSerializer))
    def get_paises(self):
        result = []
        pais_serializer = PaisSerializer()
        paises = models.Pais.objects.all()

        for pais in paises:
            pais_serializer.descripcion = pais.descripcion
            pais_serializer.valor = pais.valor
            result.append(pais_serializer)

        return result

    @soap(Integer, _returns=Array(String))
    def get_pais(self, pais_id):
        result = []
        pais = models.Pais.objects.get(pk=pais_id)

        result.append(pais.descripcion)
        result.append(pais.valor)

        return result

    """
    @soap(String,_returns=Boolean)
    def xml(self,xml):
        result = xml
        return True

    @soap(String,_returns=String)
    def xml2(self,xml2):
        return xml2
    """


class DjangoSoapApp(WSGIApplication):

    csrf_exempt = True

    def __init__(self, services, tns):
        """
        Create Django view for given SOAP soaplib services and
        tns
        """
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

my_soap_service = DjangoSoapApp([HelloWorldService], __name__)