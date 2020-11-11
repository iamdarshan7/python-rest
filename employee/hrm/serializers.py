from rest_framework import serializers
from hrm.models import User

class UserSerializer(serializers.ModelSerializer):
    employee_id = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    ranking = serializers.IntegerField(required=False)

    class Meta:
        model = User
        fields = '__all__'