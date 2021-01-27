from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HelloSerializer
from rest_framework import status


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIView features"""

        an_apiview = [
            "Uses HTTP methods as function (get, post, put, delete)",
            "Is mapped manually to URL's"
        ]

        return Response({
            "message":"Hello",
            "an_apiview": an_apiview
        })

    def post(self, request):
        """Create a hello message with our name"""

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!!!'
            return Response({
                'message':message
            })
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({
            'Method':'PUT'
        })

    def patch(self, request, pk=None):
        return Response({
            'method':'PATCH'
        })
    
    def delete(self, request, pk=None):
        return Response({
            'method':'DELETE'
        })



    