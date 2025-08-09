# utils/decorators.py

from functools import wraps
from rest_framework.response import Response
from rest_framework import status
from user.models import Professional

def require_professional(view_func):
    @wraps(view_func)
    def _wrapped_view(self, request, *args, **kwargs):
        try:
            professional = request.user.professionals.get()
        except Professional.DoesNotExist:
            return Response(
                {"detail": "User is not a professional."},
                status=status.HTTP_403_FORBIDDEN
            )
        # Añadir el profesional al request para usarlo en la vista
        request.professional = professional
        return view_func(self, request, *args, **kwargs)
    return _wrapped_view
