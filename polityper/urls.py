"""polityper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from rest_framework_jwt.views import verify_jwt_token

app_name = "polityper"

urlpatterns = [
    # admin panel
    path('admin/', admin.site.urls),
    # swagger endpoints
    path('api/schema/', get_schema_view(title='wpam-project', description='WPAM-Projekt', version='0.0.0'), name='openapi-schema'),
    path('api/swagger/', TemplateView.as_view(template_name='swagger-ui.html', extra_context={'schema_url': 'openapi-schema'}), name='swagger-ui'),
    # auth endpoints
    path('auth/', include('rest_auth.urls')),
    path('auth/registration/', include('rest_auth.registration.urls')),
    path('auth/verify', verify_jwt_token),
    # apps endpoints
    path('api/teams/', include("teams.api", namespace='teams-api')),
    path('api/betting/', include("betting.api", namespace='betting-api')),
    # login views
    path('account/', include('django.contrib.auth.urls')),
    # apps views
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('teams/', include("teams.urls", namespace='teams'))
]
