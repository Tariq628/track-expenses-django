from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("expenses/", include("expenses.urls")),
    path("", include("home.urls")),
]
