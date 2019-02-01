from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListAPIView,CreateAPIView,ListCreateAPIView
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import HelloWorldSerializer,SubscriberSerializer
from .models import Subscriber


@api_view(['POST'])
def login(request):

	username = request.data.get("username")
	password = request.data.get("passsword")

	user = authenticate(username=username,password=password)
	if not user:
		return Response({"error" : "Login Failed"},status=HTTP_401_UNAUTHORIZED)
	
	token, _ = Token.objects.get_or_create(user=user)
	return Response({"token":token.key})

class HelloWorldView(APIView):
	def get(self,request):
		return Response({"message":"Hello World!"})

	def post(self,request):
		serializer = HelloWorldSerializer(data=request.data)
		if serializer.is_valid():
			valid_data = serializer.data

			name = valid_data.get("name")
			age  = valid_data.get("age")
			return Response({"message":"Hello {},you're {} years old".format(name,age)})
		else:
			return Response({"errors":serializer.errors})		

class SubscriberViewSet(ModelViewSet):
	serializer_class = SubscriberSerializer
	queryset = Subscriber.objects.all()
	permission_classes = (IsAuthenticated,)

class SubscriberView(ListCreateAPIView):
	serializer_class = SubscriberSerializer
	queryset = Subscriber.objects.all()
	def get(self,request):
		all_subscribers = Subscriber.objects.all()
		serialized_subscribers = SubscriberSerializer(all_subscribers,many=True)
		return Response({"message":"Hello World !!"})

	def post(self,request):
		serializer = SubscriberSerializer(data=request.data)
		if serializer.is_valid():
			subscriber_instance = Subscriber.objects.create(**serializer.data)
			return Response({"message":"Created subscriber {}".format(subscriber_instance)})
		else:
			return Response({{"errors":serializer.errors}})

def hello_world(request):
	return JsonResponse({"message":"hello world"})
