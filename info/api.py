from django.http import JsonResponse
from rest_framework.views import APIView


class UpdateUserAPI(APIView):
    permission_class = []
    authentication_class = []

    def post(self, request):
        return JsonResponse("ok")