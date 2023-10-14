from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name="home"),
    path('login/', views.loginuser, name="login"),
    path('register/', views.reg, name="register"),
    path('logout/', views.logoutuser, name="logout"),
    path('reset-password/', views.reset_password, name="reset_password"),
    path('reset-password/done/', views.reset_password_done, name="password_reset_done"),
    path('reset-password/confirm/<uidb64>/<token>/', views.reset_password_confirm, name="password_reset_confirm"),
    path('reset-password/complete/', views.reset_password_complete, name="password_reset_complete"),
]
