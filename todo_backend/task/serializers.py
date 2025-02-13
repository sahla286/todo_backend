from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task
import bleach
from datetime import date

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password']
        
    def create(self,validated_data):
        return User.objects.create_user(**self.validated_data)


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields="__all__"
        extra_kwargs = {"user": {"read_only": True}}  

    def validate_description(self, value):
        return bleach.clean(value) 

    def validate_due_date(self, value):
        if value < date.today():
            raise serializers.ValidationError("Due date cannot be in the past.")
        return value