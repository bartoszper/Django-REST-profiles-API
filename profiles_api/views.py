from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HelloSerializer
from rest_framework import status
from rest_framework import viewsets


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


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = HelloSerializer

    def list(self, request):
        """Return hello message"""

        an_apiview =[
            'Uses actions (list, create, retrive, update, partial_update, destroy)'
        ]
        return Response(
            {'message': an_apiview}
        )

    def create(self, request):
        """Create a new hello message"""

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message':message})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        """Handle getting object by its ID"""
        return Response({'method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating object """
        return Response({"method": 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle partial update """
        return Response({'method': 'PATCH'})

    def destroy(self, response, pk=None):
        """Delete an object"""
        return Response({'message':'DELETE'})
    