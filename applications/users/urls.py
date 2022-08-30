from django.urls import path
from . import views

app_name = 'users_app'

urlpatterns = [
    path(
        'list_users/', 
        views.UsersListView.as_view(), 
        name='list-users'
        ),
    path(
        'register/', 
        views.UserRegisterView.as_view(), 
        name='user-register'
        ),
    path(
        'login/', 
        views.Login.as_view(), 
        name='user-login'
        ),
    path(
        'user_update/<pk>/', 
        views.UserUpdateView.as_view(), 
        name='user-update'
        ),
    path(
        'user_active/<pk>/', 
        views.UserActiveView.as_view(), 
        name='user-active'
        ),
    path(
        'logout/', 
        views.LoguotView.as_view(), 
        name='user-logout'
        ),
    path(
        'update_pass/', 
        views.UpdatePasswordView.as_view(), 
        name='update-pass'
        ),
    path(
        'user_delete/<pk>/', 
        views.UserDeleteView.as_view(),
        name='user-delete',
    ),
    
    # apis
    path(
        'api/users/list/',
        views.UsersListApiView.as_view(),
    ),
]

