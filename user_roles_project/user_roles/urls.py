from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.create_user, name='create_user'),
    path('users/<int:pk>/', views.update_user, name='update_user'),
    path('users/<int:pk>/disable/', views.disable_user, name='disable_user'),
    path('users/<int:pk>/assign_role/', views.assign_role, name='assign_role'),
]