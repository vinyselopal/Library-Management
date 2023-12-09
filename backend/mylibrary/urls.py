from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

urlpatterns = [
    path("", lambda request: redirect("librarymanagement/")),
    path("librarymanagement/", include("librarymanagement.urls")),
    path("admin/", admin.site.urls),
]
