# Create your views here.
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import UserSerializer, UserLoginSerializer, UserDetailSerializer
from webpush import send_user_notification


class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        unhashed_pwd = serializer.validated_data["password"]
        hashed_pwd = make_password(unhashed_pwd, None, "md5")
        serializer.save(password=hashed_pwd)


class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        payload = {"head": "Welcome!", "body": "Hello World"}
        print(self.request.user)

        user = User.objects.get(email=self.request.user)
        send_user_notification(user=user, payload=payload, ttl=1000)
        # Here in the user parameter, a user object should be passed
        # The user will get notification to all of his subscribed browser. A user can subscribe many browsers.
        serializer.save()


class UserLoginView(APIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

    error_messages = {
        'invalid': "Invalid username or password",
        'disabled': "Sorry, this account is suspended",
    }

    def _error_response(self, message_key):
        data = {
            'success': False,
            'message': self.error_messages[message_key],
            'user_id': None,
        }

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                data = get_tokens_for_user(user)
                return Response(data, status=status.HTTP_200_OK)
            return self._error_response('disabled')
        return self._error_response('invalid')


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
