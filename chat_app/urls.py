from django.contrib.auth import views as auth_views
from django.urls import path

from .views import CustomLoginView, frontpage, signup

urlpatterns = [
    path ('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('login/', CustomLoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]