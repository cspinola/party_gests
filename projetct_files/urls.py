from django.contrib import admin
from django.urls import path
from party_guests import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home')
    path('guests/', views.guests, name='guests')
]
