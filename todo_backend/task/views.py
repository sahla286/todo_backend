# from django.shortcuts import render
# from .models import *
# from .serializers import *
# from django.contrib.auth.models import User
# from rest_framework.decorators import api_view
# from rest_framework import viewsets, filters
# from rest_framework.response import Response
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework_simplejwt.tokens import RefreshToken
# from django.contrib.auth import authenticate
# from django.http import JsonResponse



# # Create your views here.





# @api_view(['POST'])
# def register_user(request):
#     """ Register a new user """
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         user = serializer.save()
#         refresh = RefreshToken.for_user(user)
#         return Response({
#             'user': serializer.data,
#             'refresh': str(refresh),
#             'access': str(refresh.access_token)
#         }, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# def login_user(request):
#     """ Login user and return JWT token """
#     username = request.data.get('username')
#     password = request.data.get('password')
    
#     user = authenticate(username=username, password=password)
#     if user:
#         refresh = RefreshToken.for_user(user)
#         return Response({
#             'refresh': str(refresh),
#             'access': str(refresh.access_token),
#         }, status=status.HTTP_200_OK)
#     return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

# # @api_view(['POST'])
# # def logout_user(request):
# #     """ Logout user by blacklisting the refresh token """
# #     refresh_token = request.data.get('refresh')
# #     if not refresh_token:
# #         return Response({'error': 'Refresh token is required'}, status=status.HTTP_400_BAD_REQUEST)

# #     try:
# #         token = RefreshToken(refresh_token)
# #         token.blacklist()
# #         return Response({'message': 'Successfully logged out'}, status=status.HTTP_200_OK)
# #     except Exception:
# #         return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def logout_user(request):
#     refresh_token = request.data.get('refresh')
    
#     if not refresh_token:
#         return Response({'error': 'Refresh token is missing'}, status=status.HTTP_400_BAD_REQUEST)

#     try:
#         token = RefreshToken(refresh_token)
#         token.blacklist()
#         return Response({'message': 'Successfully logged out'}, status=status.HTTP_200_OK)
#     except Exception as e:
#         return Response({'error': f'Invalid token: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)



# # class TaskViewSet(viewsets.ModelViewSet):
# #     queryset = Task.objects.all()
# #     serializer_class = TaskSerializer
# #     filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
# #     filterset_fields = ['status', 'due_date']
# #     ordering_fields = ['due_date']
# #     search_fields = ['title', 'description']


# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import TokenAuthentication

# class TaskViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#     filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
#     filterset_fields = ['status', 'due_date']
#     ordering_fields = ['due_date']
#     search_fields = ['title', 'description']
#     permission_classes = [IsAuthenticated]  # Ensure only logged-in users can update
#     # authentication_classes = [TokenAuthentication]


# # from rest_framework.permissions import IsAuthenticated
# # from rest_framework.authentication import TokenAuthentication

# # class TaskViewSet(viewsets.ModelViewSet):
# #     queryset = Task.objects.all()
# #     serializer_class = TaskSerializer
# #     authentication_classes = [TokenAuthentication]
# #     permission_classes = [IsAuthenticated]

# #     def perform_create(self, serializer):
# #         serializer.save(user=self.request.user)



# # from rest_framework.permissions import IsAuthenticated
# # from rest_framework import viewsets
# # from rest_framework.response import Response
# # from rest_framework import status
# # from .models import Task
# # from .serializers import TaskSerializer

# # class TaskViewSet(viewsets.ModelViewSet):
# #     serializer_class = TaskSerializer
# #     permission_classes = [IsAuthenticated]  # Ensure only authenticated users can access
    
# #     def get_queryset(self):
# #         """ Return tasks that belong to the logged-in user """
# #         return Task.objects.filter(user=self.request.user)  # Filter by the logged-in user

# #     def perform_create(self, serializer):
# #         """ Assign the logged-in user as the task owner when creating a task """
# #         serializer.save(user=self.request.user)

# #     def update(self, request, *args, **kwargs):
# #         """ Ensure only the task owner can update """
# #         task = self.get_object()
# #         if task.user != request.user:
# #             return Response({'error': 'You are not allowed to update this task'}, status=status.HTTP_403_FORBIDDEN)
# #         return super().update(request, *args, **kwargs)

# #     def destroy(self, request, *args, **kwargs):
# #         """ Ensure only the task owner can delete """
# #         task = self.get_object()
# #         if task.user != request.user:
# #             return Response({'error': 'You are not allowed to delete this task'}, status=status.HTTP_403_FORBIDDEN)
# #         return super().destroy(request, *args, **kwargs)

# # from rest_framework.permissions import IsAuthenticated

# # class TaskViewSet(viewsets.ModelViewSet):
# #     queryset = Task.objects.all()
# #     serializer_class = TaskSerializer
#     # permission_classes = [IsAuthenticated] 


# from datetime import datetime

# @api_view(['GET'])
# def calendar_tasks(request):
#     """ Return tasks formatted for FullCalendar.js """
#     tasks = Task.objects.all()
#     task_list = [
#         {
#             "id": task.id,
#             "title": task.title,
#             "start": task.due_date.strftime("%Y-%m-%d"),  # Convert to string
#             "status": task.status
#         }
#         for task in tasks
#     ]
#     return JsonResponse(task_list, safe=False)






# from django.shortcuts import render
# from rest_framework.viewsets import ModelViewSet,ViewSet
# from rest_framework.filters import OrderingFilter
# from rest_framework import authentication, permissions, status
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.exceptions import NotFound
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from django.db.models import Count
# from datetime import date
# from django_filters.rest_framework import DjangoFilterBackend 
# from .serializers import *
# from .models import *
# from django.http import JsonResponse

# class UserViewset(ViewSet):
#     def create(self,request):
        
#         ser=UserSerializer(data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(data=ser.data,status=status.HTTP_201_CREATED)
#         return Response(data={"error":ser.errors},status=status.HTTP_400_BAD_REQUEST)

# class TaskView(ModelViewSet):
#     serializer_class = TaskSerializer
#     queryset = Task.objects.all()
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [permissions.IsAuthenticated]
#     filter_backends = [DjangoFilterBackend, OrderingFilter]
#     filterset_fields = ['status', 'due_date']
#     ordering_fields = ['due_date', 'title']
#     ordering = ['due_date']



#     def perform_create(self, serializer):
        
#         serializer.save(user=self.request.user)

#     def get_queryset(self):
#         return Task.objects.filter(user=self.request.user)
    
#     # def get_object(self):
#     #     obj = super().get_object()
#     #     if obj.user != self.request.user:
#     #         raise NotFound({"error": "Task not found or access denied."})
#     #     return obj

# # @api_view(['GET'])
# # def calendar_tasks(request):
# #     if not request.user.is_authenticated:
# #         return Response({"error": "Authentication required."}, status=status.HTTP_401_UNAUTHORIZED)

# #     # Optimize query: Get all tasks with user filter
# #     tasks = Task.objects.filter(user=request.user).order_by('due_date')

# #     # Organizing tasks by date
# #     task_dict = {}
# #     for task in tasks:
# #         due_date = task.due_date
# #         if due_date not in task_dict:
# #             task_dict[due_date] = {"due_date": due_date, "task_count": 0, "tasks": []}
# #         task_dict[due_date]["task_count"] += 1
# #         task_dict[due_date]["tasks"].append({
# #             "id": task.id,
# #             "title": task.title,
# #             "status": task.status
# #         })

# #     return Response(list(task_dict.values()))




# @api_view(['GET'])
# def calendar_tasks(request):
#     """ Return tasks formatted for FullCalendar.js """
#     tasks = Task.objects.all()
#     task_list = [
#         {
#             "id": task.id,
#             "title": task.title,
#             "start": task.due_date.strftime("%Y-%m-%d"),  # Convert to string
#             "status": task.status
#         }
#         for task in tasks
#     ]
#     return JsonResponse(task_list, safe=False)


from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .models import Task
from .serializers import TaskSerializer, UserSerializer

class UserViewSet(ViewSet):
    """
    ViewSet for User Registration
    """
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskViewSet(ModelViewSet):
    """
    ViewSet for handling Task CRUD operations
    """
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['status', 'due_date']
    ordering_fields = ['due_date', 'title']
    ordering = ['due_date']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([permissions.IsAuthenticated])
def calendar_tasks(request):
    """
    Retrieve tasks formatted for FullCalendar.js
    """
    tasks = Task.objects.filter(user=request.user)
    task_list = [
        {
            "id": task.id,
            "title": task.title,
            "start": task.due_date.strftime("%Y-%m-%d"),
            "status": task.status
        }
        for task in tasks
    ]
    return Response(task_list)
