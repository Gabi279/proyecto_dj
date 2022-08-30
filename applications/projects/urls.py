from django.urls import path
from . import views

app_name = 'project_app'

urlpatterns = [
    path('proyectos/', 
        views.ProjectView.as_view(),
        name='proyectos'
    ),
    path('projects_users/', 
        views.ProjectUserView.as_view(),
        name='projects-users'
    ),
    path('new_project/', 
        views.ProyectoCreateView.as_view(),
        name='new-project'
    ),
    path('new_project_user/', 
        views.ProyectoUserCreateView.as_view(),
        name='new-project-user'
    ),
    path(
    'project_update/<pk>/', 
    views.ProjectUpdateView.as_view(), 
    name='project-update'
    ),
    path(
    'project_active_p/<pk>/', 
    views.ProjectActiveView.as_view(), 
    name='project-active-p'
    ),
    path(
    'project_delete/<pk>/', 
    views.ProjectDeleteView.as_view(),
    name='project-delete',
    ),
    
    # apis
    path(
        'api/projects/list/',
        views.ProjectsListApiView.as_view(),
    ),
]