from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
	"""Test API view"""

	def get(self, request, format=None):
		"""Return a list of APIView features"""
		an_apiview = [
			 'Uses HTTP methods as function (get, post, patch, push, delete)',
			 'Is similar to a traditional Django view',
			 'Gives you the most control over your API logic',
			 'Is mapped manually to URLs',
		]

		return Response({'message': 'Hello!', 'an_apiview': an_apiview})
