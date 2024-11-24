from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .serializers import UserSerializer
from .models import UserProfile
from .forms import RegisterForm
from .tasks import send_verification_email
import secrets
from django.shortcuts import render

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Login a user with email and password",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='User email'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='User password'),
            },
            required=['email', 'password'],
        ),
        responses={
            200: "Login successful",
            400: "Invalid credentials",
        },
    )
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Logout the current user",
        responses={200: "Logout successful"},
    )
    def post(self, request):
        logout(request)
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)


class RegisterAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Register a new user",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='User email'),
            },
            required=['email'],
        ),
        responses={
            200: "Verification email sent",
            400: "User with this email already exists or invalid data",
        },
    )
    def post(self, request):
        form = RegisterForm(request.data)
        if form.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                return Response({'error': 'User with this email already exists'}, status=status.HTTP_400_BAD_REQUEST)
            confirmation_code = secrets.token_hex(3)
            request.session['confirmation_code'] = confirmation_code
            request.session['email'] = email
            send_verification_email.delay(email, confirmation_code)
            return Response({'message': 'Verification email sent'}, status=status.HTTP_200_OK)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyEmailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Verify the email with a confirmation code",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'code': openapi.Schema(type=openapi.TYPE_STRING, description='Confirmation code'),
            },
            required=['code'],
        ),
        responses={
            200: "Email verified successfully",
            400: "Invalid confirmation code",
        },
    )
    def post(self, request):
        code = request.data.get('code')
        if code == request.session.get('confirmation_code'):
            return Response({'message': 'Email verified successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid confirmation code'}, status=status.HTTP_400_BAD_REQUEST)


class SetPasswordAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Set a password for the user",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='User password'),
                'confirm_password': openapi.Schema(type=openapi.TYPE_STRING, description='Confirm password'),
            },
            required=['password', 'confirm_password'],
        ),
        responses={
            200: "Password set successfully",
            400: "Passwords do not match",
        },
    )
    def post(self, request):
        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')
        if password == confirm_password:
            email = request.session.get('email')
            user = User.objects.create_user(email, email, password)
            UserProfile.objects.create(user=user)
            return Response({'message': 'Password set successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)


class MainAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Get the main welcome page",
        responses={200: "Main welcome page"},
    )
    def get(self, request):
        if request.user.is_authenticated:
            return Response({'message': f'Welcome, {request.user.username}'}, status=status.HTTP_200_OK)
        else:
            return render(request, 'accounts/main.html')
