
from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.sign_up, name="sign_up"),
    path('logout/', views.logout, name="log_out"),
    path('login/',views.login, name="login"),
]