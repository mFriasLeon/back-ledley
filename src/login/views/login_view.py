from login.serializers.login_serializer import LoginRequestSerializer, TokenResponseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from user.models import User
from drf_spectacular.utils import extend_schema
class LoginView(APIView):
    @extend_schema(
        request=LoginRequestSerializer,
        responses={
            200: TokenResponseSerializer,
            400: "Bad Request",
            401: "Unauthorized",
            403: "Forbidden"
        },
        summary="User Login",
        description="Endpoint for user login, returns JWT tokens if credentials are valid."
    )
    def post(self, request):
        import ipdb; ipdb.set_trace()
        serializer = LoginRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        username = serializer.validated_data.get("username")
        password = serializer.validated_data.get("password")                            

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        if not user.active:
            return Response({"detail": "Account is inactive"}, status=status.HTTP_403_FORBIDDEN)

        if not check_password(password, user.password):
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)

        response_serializer = TokenResponseSerializer({
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        })

        return Response(
            response_serializer.data,
            status=status.HTTP_200_OK
        )
