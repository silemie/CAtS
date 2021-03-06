"""webapps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views
from cas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_action, name='login'),
    path('register', views.register_action, name='register'),
    path('projects', views.get_project_list_action, name='projects'),
    path('config_project', views.get_project_configuration, name='config_project'),
    path('get_project_controlls', views.get_project_controlls, name='project_controls'),
    path('new_project', views.create_project_action, name='new_project'),
    path('search_projects', views.search_projects_action, name='search_projects'),
    path('controls', views.get_control_list_action, name='controls'),
    path('get_control_by_id', views.get_control_by_id_action, name='get_control_by_id'),
    path('searchControls', views.search_control_list_action, name='controls'),
    path('search/<int:id>/', views.search_project_by_id, name='search_project_by_id'),
    path('update/<int:id>/', views.update_project, name='update_project'),
    path('delete', views.delete_project, name='delete_project'),
    path('setcontrols', views.configure_control_action, name='configure_controls'),
    path('project_dashboard', views.project_dashboard, name='project_dashboard'),
    path('parse_report', views.parse_testing_report, name='parse_report'),
    path('get_controlconfig_by_id', views.get_controlconfig_by_id, name='get_controlconfig_by_id'),
    path('get_reports', views.get_reports, name='get_reports'),
    path('get_issues', views.get_issues, name='get_issues'),
    path('logout', views.logout_action, name='logout'),
    path('profile', views.get_profile_action, name='get_profile'),
    path('update_profile', views.update_profile_action, name='update_profile_info'),
    path('setting', views.get_setting_action, name='get_setting'),
    path('change_password/<int:id>/', views.change_password_action, name='change_password'),
    path('share_project/<int:id>/', views.share_project_action, name='share'),
    path('stop_share_project/<int:id>/', views.stop_share_project_action, name="stop_share"),
    path('shared_projects', views.get_shared_project_list_action, name='get_shared_project'),
    path('get_id_by_name', views.get_id_from_name, name='get_id_by_name'),
    path('get_name_by_id', views.get_name_from_id, name='get_name_by_id'),
    path('detail', views.get_details, name='get_detail'),
    path('enter_credential', views.enter_credential_action, name='enter_credential'),
]
