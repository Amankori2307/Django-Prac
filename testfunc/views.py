from rest_framework import views
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.response import Response

# Create your views here.

class AuthTest(views.APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, BasicAuthentication]

    def get(self, request):
        return Response("Well i am autheticated")