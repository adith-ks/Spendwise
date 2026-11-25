from rest_framework import serializers
from .models import Expense # . > import from the current app
from django.contrib.auth.models import User
class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = "__all__" #it means all fields of the Expense model will be included in the serialized representation.
        ready_only_fields = ['user',    'created_at', 'updated_at'] #it means that these fields will be included in the serialized representation, but they cannot be modified when creating or updating an expense through the API.


class RegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
