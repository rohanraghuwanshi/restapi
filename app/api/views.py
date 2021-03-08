from rest_framework.views import APIView
from rest_framework.response import Response

from app.models import Status
from .serializers import StatusSerializer

class StatusListSearchAPIView(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, format=None):
        qs = Status.objects.all()
        serialzer = StatusSerializer(qs, many=True)
        return Response(serialzer.data)