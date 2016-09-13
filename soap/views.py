"""
from django.views.generic import TemplateView

from soap import SoapView
from soaplib.core.service import soap
from soaplib.core.model.primitive import String, Integer

# Create your views here.


class Soap(TemplateView):

    template_name = 'soap.html'

    def get(self, request, *args, **kwargs):

        from suds.client import Client
        cliente1 = Client('http://localhost:8000/verify.wsdl')
        #result = cliente1.service.request_verify("Dave", 5, "nada")
        print cliente1.service


class MySoapService(SoapView):
    __tns__ = '[url]http://localhost:8000/verify.wsdl[/url]'

    @soap(String, Integer, returns=String)
    def request_verify(self, q, id, uri):
        #Some Code
        return 'some return'

    @soap(String, Integer, Integer, Integer, returns=String)
    def request_hola_mundo(self, nombre, num1, num2, num3, nombre2):
        #Some Code
        return 'HOLA MUNDO!'


class HolaMundo(SoapView):
    __tns__ = '[url]http://localhost:8000/hola.wsdl[/url]'

    @soap(String, Integer, Integer, Integer, returns=String)
    def request_hola_mundo(self, nombre, num1, num2, num3, nombre2):
        #Some Code
        return 'HOLA MUNDO!'


my_soap_service = MySoapService.as_view()
soap_hola_mundo = HolaMundo.as_view()
"""

from soaplib.core.service import rpc, DefinitionBase, soap
from soaplib.core.model.primitive import String, Integer, Boolean, DateTime
from soaplib.core.model.clazz import Array
from soaplib.core import Application
from soaplib.core.server.wsgi import Application as WSGIApplication
from django.http import HttpResponse


class HelloWorldService(DefinitionBase):

    @soap(String, String, String, String)
    def SpotsPorProductosAnunciante(self, codigo_Plaza, codigo_Vehiculo,
            fechaDesde, fechaHasta):
        return "defSpotsPorProductosAnunciante"

    @soap(Integer, DateTime, DateTime, Integer, String, Integer, Integer,
          String, String, Integer, String, String)
    def EvaluacionSpotInfoCompletaPorProdAnunciante(self, Region, Fecha,
            Minuto, CodigoTema, Tema, Duracion, Canal, Anunciante, Producto,
            CodigoMaterial, Matrerial, LTargetRatingsInfo):
        return "def EvaluacionSpotInfoCompletaPorProdAnunciante"

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