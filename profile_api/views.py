from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profile_api import serializers
from profile_api import models
from profile_api import permissions

class HelloApiView(APIView):
    """test Api View."""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """return a list of APIView features"""
        an_apiView = [
            'User HTTP methods as funtion (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'gives you the most control over you app logic',
            'Is mapped manually to URLS',
        ]

        return Response({'message': 'Hello', 'an_apiView': an_apiView})

    def post(self, request):
        """create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')

            message = f'Hello, {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """hanle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """handle delete an object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """test api ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """ return a hello message """
        a_viewset = [
            'users actions (list, create, retrieve, update, patial_update)',
            'auto maps to URLs using Routers',
            'Provides more funtionality with less code',
        ]

        return  Response({'message': 'Hello! using viewset', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """handle getting an object by its id, 访问需要后面加/序号"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """handle updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """handle updating part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """handle removing an object"""
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
