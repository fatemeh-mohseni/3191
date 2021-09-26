from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_user , name = 'userapp_login'),
    path('register/', views.register , name = 'userapp_register'),  # href="{% url 'userapp_register' %}"
]   # names should be string