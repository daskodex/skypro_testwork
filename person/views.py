from django.http import JsonResponse
from django.shortcuts import render


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.views import APIView

from .serializers import SimplePersonSerializer
from .models import SimplePerson

# Create your tests here.


class PersonListView(generics.ListAPIView):
    queryset = SimplePerson.objects.all()
    serializer_class = SimplePersonSerializer


@permission_classes([IsAuthenticated])
class PersonDetailView(APIView):
    def get_object(self, pk):
        return SimplePerson.objects.get(pk=pk)

    def patch(self, request, pk):
        testmodel_object = self.get_object(pk)
        serializer = SimplePersonSerializer(testmodel_object, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data)
        return JsonResponse(data="wrong parameters")