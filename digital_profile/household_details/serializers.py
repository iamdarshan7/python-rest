
from rest_framework import serializers
from .models import HouseholdDetails


class HouseholdDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = HouseholdDetails
        fields = "__all__"
