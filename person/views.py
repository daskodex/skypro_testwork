from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, BasePermission
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SimplePersonSerializer
from .models import SimplePerson


# Create your tests here.


class PersonListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]

    queryset = SimplePerson.objects.all()
    serializer_class = SimplePersonSerializer


class PersonDetailView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk):
        try:
            test_model_object = SimplePerson.objects.get(pk=pk)
        except SimplePerson.DoesNotExist:
            return Response({'error': 'Object does not exist'}, status=404)

        serializer = SimplePersonSerializer(test_model_object, many=False)
        return JsonResponse(data=serializer.data, status=200)

    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        try:
            test_model_object = SimplePerson.objects.get(pk=pk)
        except SimplePerson.DoesNotExist:
            return Response({'error': 'Object does not exist'}, status=404)

        serializer = SimplePersonSerializer(test_model_object, data=request.data,
                                            partial=True)  # set partial=True to update a data partially

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=201)

        return JsonResponse(data="Wrong parameters")
