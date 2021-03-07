from django.conf import settings
from xhtml2pdf import pisa
from io import BytesIO
from django.template.loader import get_template
from django.http import HttpResponse

def gen_response(error, success, message = "", data = {}):
    return {
        "error": error,
        "success": success,
        "message" : message,
        "data": data
    }

def render_to_pdf(template_path, context):
    template = get_template(template_path)
    html = template.render(context)
    result = BytesIO()

    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type="application/pdf")
    else:
        return None

import os
from django.conf import settings
def get_absolute_path(uri):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    # use short variable names
    sUrl = settings.STATIC_URL      # Typically /static/

    # convert URIs to absolute system paths
    path = os.path.join(settings.BASE_DIR, "static", uri)

    # make sure that file exists
    print(settings.BASE_DIR)
    print(path)
    # if not os.path.isfile(path):
    #         raise Exception('File Not Found')
    return path