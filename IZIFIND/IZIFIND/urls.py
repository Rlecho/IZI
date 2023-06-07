"""
IZIFIND URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path
from accounts import views
from accounts.views import RegisterView, user_list, login_view, password_reset_view, password_change_view

app_name='accounts'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('insc/', views.inscription , name='insc'),
    path('connect/', views.connexion , name='connect'),
    path('connects/', views.change_password , name='connects'),
    path('reset/', views.reset_password , name='reset'),
    path('register/', RegisterView.as_view(), name='register'),
    path('users/', user_list, name='user_list'),
    path('login/', login_view, name='login'),
    # path('password/reset/', password_reset_view, name='password_reset'),
    # path('password/change/', password_change_view, name='password_change'),
# ...

    path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_password_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset_password_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    
]


