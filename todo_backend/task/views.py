from django.shortcuts import render
from .models import *
from .serializers import *
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework import viewsets, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.http import JsonResponse



# Create your views here.





@api_view(['POST'])
def register_user(request):
    """ Register a new user """
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'user': serializer.data,
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_user(request):
    """ Login user and return JWT token """
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(username=username, password=password)
    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def logout_user(request):
#     """ Logout user by blacklisting the refresh token """
#     refresh_token = request.data.get('refresh')
#     if not refresh_token:
#         return Response({'error': 'Refresh token is required'}, status=status.HTTP_400_BAD_REQUEST)

#     try:
#         token = RefreshToken(refresh_token)
#         token.blacklist()
#         return Response({'message': 'Successfully logged out'}, status=status.HTTP_200_OK)
#     except Exception:
#         return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def logout_user(request):
    refresh_token = request.data.get('refresh')
    
    if not refresh_token:
        return Response({'error': 'Refresh token is missing'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({'message': 'Successfully logged out'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': f'Invalid token: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)



# class TaskViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#     filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
#     filterset_fields = ['status', 'due_date']
#     ordering_fields = ['due_date']
#     search_fields = ['title', 'description']


from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['status', 'due_date']
    ordering_fields = ['due_date']
    search_fields = ['title', 'description']
    permission_classes = [IsAuthenticated]  # Ensure only logged-in users can update
    # authentication_classes = [TokenAuthentication]


# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import TokenAuthentication

# class TaskViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)



# from rest_framework.permissions import IsAuthenticated
# from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Task
# from .serializers import TaskSerializer

# class TaskViewSet(viewsets.ModelViewSet):
#     serializer_class = TaskSerializer
#     permission_classes = [IsAuthenticated]  # Ensure only authenticated users can access
    
#     def get_queryset(self):
#         """ Return tasks that belong to the logged-in user """
#         return Task.objects.filter(user=self.request.user)  # Filter by the logged-in user

#     def perform_create(self, serializer):
#         """ Assign the logged-in user as the task owner when creating a task """
#         serializer.save(user=self.request.user)

#     def update(self, request, *args, **kwargs):
#         """ Ensure only the task owner can update """
#         task = self.get_object()
#         if task.user != request.user:
#             return Response({'error': 'You are not allowed to update this task'}, status=status.HTTP_403_FORBIDDEN)
#         return super().update(request, *args, **kwargs)

#     def destroy(self, request, *args, **kwargs):
#         """ Ensure only the task owner can delete """
#         task = self.get_object()
#         if task.user != request.user:
#             return Response({'error': 'You are not allowed to delete this task'}, status=status.HTTP_403_FORBIDDEN)
#         return super().destroy(request, *args, **kwargs)

# from rest_framework.permissions import IsAuthenticated

# class TaskViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
    # permission_classes = [IsAuthenticated] 


from datetime import datetime

@api_view(['GET'])
def calendar_tasks(request):
    """ Return tasks formatted for FullCalendar.js """
    tasks = Task.objects.all()
    task_list = [
        {
            "id": task.id,
            "title": task.title,
            "start": task.due_date.strftime("%Y-%m-%d"),  # Convert to string
            "status": task.status
        }
        for task in tasks
    ]
    return JsonResponse(task_list, safe=False)

