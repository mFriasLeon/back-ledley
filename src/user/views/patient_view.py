# user/views.py

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import CareTeamAssignment
from user.serializers import PatientSerializer
from rest_framework import status
from plan.auth_tools.decorators import require_professional

class ProfessionalPatientsView(APIView):
    permission_classes = [IsAuthenticated]

    @require_professional
    def get(self, request):
        assignments = CareTeamAssignment.objects.filter(
            professional=request.professional
        ).select_related("patient")

        serializer = PatientSerializer(assignments, many=True)
        return Response(serializer.data)
