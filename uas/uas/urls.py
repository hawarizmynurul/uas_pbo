"""uas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from SD.views import *
from SD import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", views.registerPage, name='register'),
    path("login/", views.login, name='login'),
    path("logout/", views.logoutUser, name='logout'),
    path("sekolah/", sekolah),
    path("tambah_SD/", tambah_SD),
    path("books/update_SD/<int:id_books>", update_SD, name="update_SD"),
    path(r'^delete_SD/(?P<delete_id>[0-9])$', views.delete_SD, name='delete_SD'),
    path("Murid/", Murid),
    path("tambah_murid/", tambah_murid),
    path("books/update_murid/<int:id_books>", update_murid, name="update_murid"),
    path(r'^delete_murid/(?P<delete_id>[0-9])$', views.delete_murid, name='delete_murid'),
]
