from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from utils.helperfunctions import gen_response
import xlwt
from django.http import HttpResponse
from utils.arial10 import fitwidth


# Create your views here.
class CreateXLSView(APIView):
    def get(self, request):
        response = HttpResponse(content_type="applicateion/ms-excel")
        response['Content-Disposition'] = 'attachment; filename="sample.xls"'

        workbook = xlwt.Workbook(encoding="utf-8")
        sheet = workbook.add_sheet("SampleUsers")

        style = xlwt.easyxf("font: height 600, bold on, colour white; align: horz left, vert center; pattern: pattern solid, fore_colour blue")
        pattern = xlwt.Pattern()
        pattern.pattern_back_colour
        
        sheet.write_merge(
            0, 0,
            0, 10,
            "Django Prac",
            style
        )
        row_style = xlwt.easyxf("font: height 500;")
        sheet.row(1).set_style(row_style)
        style2 = xlwt.easyxf("font: height 200, italic on, underline on, colour white; align: horz left, vert center; pattern: pattern solid, fore_colour blue")
        sheet.write_merge(
            1 , 1,
            0, 10,
            "http:/django-prac/?message=hello-mate",
            style2
        )


        columns = ["ID", "Name", "Surname", "Age", "Address", "Description(About User)"]
        row = 2
        for col in range(0, len(columns)):
            sheet.write(row, col, columns[col], xlwt.easyxf("font: bold on;"))

        data = [
            [1, "Aman", "Kori", 18, 'Home No. Locality, City, State, Pin Code', "So guys this is the description"],
            [2, "Kunal", "Kori", 21, 'Home No. Locality, City, State, Pin Code', "So guys this is the description"],
            [3, "Chetna", "Kori", 10, 'Home No. Locality, City, State, Pin Code', "So guys this is the description"],
            [4, "Rekha", "Kori", 35, 'Home No. Locality, City, State, Pin Code', "So guys this is the description"],
            [5, "Klaus", "Mikaelson", 43, 'New Orleans', "My Favourite Characters From The Originals"],
        ]
        for item in data:
            row += 1
            print(item)
            for col_num in range(0, len(item)):
                sheet.write(row, col_num, item[col_num])

        # Adjusting Column widths

        #calculating width
        widths = []
        for col in range(0, len(columns)):
            widths.append(int(fitwidth(columns[col])))

        for item in data:
            for col in range(0, len(item)):
                tempWidth = int(fitwidth(str(item[col])))
                if widths[col] < tempWidth:
                    widths[col] = tempWidth

        for col in range(0, len(columns)):
            sheet.col(col).width = widths[col]+800


        workbook.save(response)
        # return Response()
        return response
