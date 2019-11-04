from django.urls import path, include
from . import views

# New url pattern below
urlpatterns = [
    path('', views.home, name='homepage'),
    path('auth/', include('django.contrib.auth.urls'), name='login'),
    path('auth/signup', views.signup, name='signup'),
    path('profile/', views.dashboard, name='user_dashboard'),
]


