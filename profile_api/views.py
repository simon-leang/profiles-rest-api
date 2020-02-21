from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """dtest Api View."""

    def get(self, request, format=None):
        """return a list of APIView features"""
        an_apiView = [
            'User HTTP methods as funtion (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'gives you the most control over you app logic',
            'Is mapped manually to URLS',
        ]

        return Response({'message': 'Hello', 'an_apiView': an_apiView})
