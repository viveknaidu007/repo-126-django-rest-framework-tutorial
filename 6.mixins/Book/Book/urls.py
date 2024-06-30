from Books import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/",admin.site.urls),
    path("api/",views.Studentlist.as_view()),
    path("add/",views.Studentcreate.as_view()),
]