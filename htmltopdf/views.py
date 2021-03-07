from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from xhtml2pdf import pisa
from django.template import loader
from django.http import HttpResponse
from io import BytesIO
from utils.helperfunctions import gen_response, render_to_pdf, get_absolute_path
from datetime import date

# Create your views here.
class HTMLToPDFView(APIView):
    def get(self, request):
        
        context = {
            "logo_url": get_absolute_path("logo.jpg"),
            "from_year": date.today().year,
            "to_year": date.today().year + 1,
            "brand_name": "Django Prac",
            "message": "I am really happy to tell you that i have successfully used XHTML2PDF module"
        }
        response = render_to_pdf('htmltopdf/dummy.html', context)
        return response


        # template = loader.get_template('htmltopdf/dummy.html')
        # context = {
        #     'latest_question_list': "latest_question_list",
        # }
        # return HttpResponse(template.render({},request))

    