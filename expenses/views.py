from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegistrationSerializer,ExpenseSerializer
from django.contrib.auth.models import User
from .models import Expense
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework import authentication



class RegistrationView(APIView):

    def post(self, request):
        serializer_instance = RegistrationSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response({"Message": "User created successfully"})
        return Response(serializer_instance.errors)

class UserView(APIView):
    def get(self,request):
        qs = User.objects.all()
        serializer_instance = RegistrationSerializer(qs,many=True)
        return Response(serializer_instance.data)

class LoginView(APIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)

            return Response({
                'message': 'Login successful',
                'token': token.key
            })

        return Response(
            {'error': 'Invalid username or password'}
        )

class ExpenseListCreateView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        qs = Expense.objects.filter(user=request.user)
        serializer_instance = ExpenseSerializer(qs, many=True)
        return Response(serializer_instance.data)

    def post(self, request):
        serializer_instance = ExpenseSerializer(data=request.data)

        if serializer_instance.is_valid():
            serializer_instance.save(user=request.user)
            return Response(serializer_instance.data)

        return Response(serializer_instance.errors)

class ExpenseRetrieveUpdateDeleteView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        qs = get_object_or_404(Expense, id=pk, user=request.user)

        serializer_instance = ExpenseSerializer(qs, data=request.data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)

        return Response(serializer_instance.errors)

    def delete(self,request,pk):
        qs = get_object_or_404(qs, id=pk, user=request.user)
        qs.delete()
        return Response({"Message":"Expense deleted successfully"})
        
