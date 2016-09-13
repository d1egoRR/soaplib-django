# -*- coding: utf-8 -*-
#import base64
#import soaplib
from soaplib.core import Application
from soaplib.core.service import DefinitionBase
from soaplib.core.server import wsgi
#from soaplib.core.model.clazz import ClassModel
#from soaplib.core.model.clazz import Array

from django.http import HttpResponse

# the class with actual web methods

# the class which acts as a wrapper between soaplib WSGI
# functionality and Django


class DjangoSoapApp(wsgi.Application):

    def __call__(self, request):
        # wrap the soaplib response into a Django response object
        django_response = HttpResponse()

        def start_response(status, headers):
            status, reason = status.split(' ', 1)
            django_response.status_code = int(status)
            for header, value in headers:
                django_response[header] = value

        response = super(DjangoSoapApp, self).__call__(
            request.META, start_response)
        django_response.content = '\n'.join(response)

        return django_response


class SoapView(DefinitionBase):

    @classmethod
    def as_view(cls):
        soap_application = Application([cls], __name__)
        return DjangoSoapApp(soap_application)


# the view to use in urls.py
#my_soap_service = DjangoSoapApp([MySOAPService], __name__)