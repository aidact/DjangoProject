from django.urls import path
from rest_framework import routers

from users import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login')
]

router = routers.DefaultRouter()
router.register(r'profiles', views.ProfileViewSet, base_name='auth')

urlpatterns += router.urls
