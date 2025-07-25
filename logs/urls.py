from django.contrib import admin
from django.urls import path, include
from app import views


urlpatterns = [
    path("admin/", admin.site.urls),
    
    path('', views.MainView.as_view(), name='main_view'),
    path('accounts/', include('allauth.urls')), 
]
