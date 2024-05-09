"""
URL configuration for todoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from todo import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register',views.SignUpView.as_view(),name="signup"),
    path('login',views.signInView.as_view(),name="signin"),
    path('index',views.IndexView.as_view(),name='index'),
    path('project/<int:pk>',views.ProjectView.as_view(),name='project-detail'),
    path('project/<int:pk>/delete',views.ProjectDeleteView.as_view(),name='project-delete'),
    path('project/<int:pk>/delete',views.TodoDeleteView.as_view(),name='todo-delete'),
    path('project/<int:pk>/status',views.TodoStatusView.as_view(),name='todo-status'),
    path('project/<int:pk>/todo-update',views.UpdateTodoView.as_view(),name='todo-update'),
    path('logout',views.LogoutView.as_view(),name="signout"),
    path('project/<int:pk>/change_title', views.ProjectTitleView.as_view(), name='update_project_title')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
