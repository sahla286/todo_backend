from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password']
        
    def create(self,validated_data):
        return User.objects.create_user(**self.validated_data)

# class TaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Task
#         fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "description", "status", "due_date", "user"]
        extra_kwargs = {"user": {"read_only": True}}  # ✅ Ensure user is read-only
