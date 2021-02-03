from django.contrib import admin
from django.urls import path, include 
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="saketh"),
    path('123', views.home, name="homepage")
    
    
]
