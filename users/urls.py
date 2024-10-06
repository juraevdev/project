from django.urls import path
from .views import user_login, user_logout, homepage, register

urlpatterns = [
    path('', homepage, name='home'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('signup/', register, name='signup'),
]