from Book import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/",admin.site.urls),
    path("api/",views.Studentde.as_view()),
]