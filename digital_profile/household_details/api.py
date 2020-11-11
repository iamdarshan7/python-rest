
from rest_framework import viewsets, permissions
from .models import HouseholdDetails
from .serializers import HouseholdDetailSerializer


class HouseholdDetailsViewSets(viewsets.ModelViewSet):
    queryset = HouseholdDetails.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = HouseholdDetailSerializer
