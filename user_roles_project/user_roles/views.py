from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from .models import Role, UserRole, CustomUser, UserLog
from .serializers import RoleSerializer, CustomUserSerializer, UserRoleSerializer
from django.core.mail import send_mail

User = get_user_model()


@api_view(['POST'])
def create_user(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save(password=make_password(request.data['password']))
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_user(request, pk):
    user = User.objects.get(pk=pk)
    serializer = CustomUserSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def disable_user(request, pk):
    user = User.objects.get(pk=pk)
    user.is_active = False
    user.save()
    return Response({'message': 'User disabled'})

@api_view(['POST'])
def assign_role(request, pk):
    user = User.objects.get(pk=pk)
    role_id = request.data.get('role')
    role = Role.objects.get(pk=role_id)
    UserRole.objects.create(user=user, role=role, is_active=True)
    UserLog.objects.create(user=user, event_type='role_assigned', data=f'Role {role.name} assigned to user {user.username}')
    return Response({'message': 'Role assigned successfully'})



@api_view(['POST'])
def create_user(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save(password=make_password(request.data['password']))
        send_mail(
            'Your account details',
            f'Username: {user.username}\nPassword: {request.data["password"]}',
            'noreply@yourdomain.com',
            [user.email],
            fail_silently=False,
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)