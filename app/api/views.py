# from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from app.models import Status
from .serializers import StatusSerializer

class StatusDetailAPIView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.RetrieveAPIView
):
    permission_classes = [IsAuthenticated,] 
    authentication_classes = [SessionAuthentication,]
    serializer_class = StatusSerializer
    queryset = Status.objects.all()    

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class StatusAPIView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.ListAPIView,
):
    permission_classes = [IsAuthenticated,]
    authentication_classes = [SessionAuthentication,]
    serializer_class = StatusSerializer

    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('query')

        if query is not None:
            qs = qs.filter(content__icontains=query)

        return qs 
    
    def get_object(self):
        request = self.request
        passed_id = request.GET.get('id', None)
        queryset = self.get_queryset()
        obj = None

        if passed_id is not None:
            obj = get_object_or_404(queryset, id=passed_id)
            self.check_object_permissions(request, obj)
        return obj

    def get(self, request, *args, **kwargs):
        passed_id = request.GET.get('id', None)

        if passed_id is not None:
            return self.retrieve(request, *args, **kwargs)
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



# class StatusListSearchAPIView(mixins.CreateModelMixin, generics.ListAPIView):
#     permission_classes = []
#     authentication_classes = []
#     serializer_class = StatusSerializer

#     def get_queryset(self):
#         qs = Status.objects.all()
#         query = self.request.GET.get('query')

#         if query is not None:
#             qs = qs.filter(content__icontains=query)

#         return qs 
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class StatusCreateAPIView(generics.CreateAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer


# Alternative way to perform all the above three operations with a single view is
# by giving in the class as generics.RetrieveUpdate,DeleteAPIView
# Instead of giving all 3 classes.

# class StatusDetailAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
        
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)



# class StatusUpdateAPIView(generics.UpdateAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer

# class StatusDeleteAPIView(generics.DestroyAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer