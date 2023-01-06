from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import*
from .form import *
from django.contrib.auth.forms import UserCreationForm
from .form import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as authlogin, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            User = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+ User)
            
            return redirect('login') 

    context = {'form':form}
    return render(request, "accounts/register.html", context)

def login(request):
    if request.user.is_authenticated:
        return redirect('/sekolah/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password )

            if user is not None:
                authlogin(request, user)
                return redirect ('/sekolah/')
            else:
                messages.info(request, 'Username atau Password salah ')
    data ={}
    return render(request, "accounts/login.html", data )

def logoutUser(request):
    logout(request)
    return redirect('login')

#@login_required(login_url='login')
def sekolah(request):
    books = Sekolah.objects.all()
    data = {
        "title"   : "Daftar Sekolah Dasar di Serang",
        "heading" : "Daftar Sekolah Dasar di Serang",
        "books"   : books,
    }
    return render(request, "sekolah.html", data)

def tambah_SD(request):
    if request.POST:
        form = FormSekolah(request.POST)
        if form.is_valid():
            form.save()
            form = FormSekolah()
            data = {
                "title" : "Tambah Data Sekolah Dasar di Serang",
                "heading" : "Tambah Data Sekolah Dasar di Serang",
                "form" : form,
                "pesan" : "Data Berhasil Ditambahkan",
            }
            return render(request, "tambah_SD.html", data)
    else:
        form = FormSekolah()
        data = {
            "title" : "Tambah Data Sekolah Dasar di Serang",
            "heading" : "Tambah Data Sekolah Dasar di Serang",
            "form" : form,
        }
        return render(request, "tambah_SD.html", data)

def update_SD(request, id_books):
    books = Sekolah.objects.get(id = id_books)
    if request.POST:
        form = FormSekolah(request.POST, instance=books)
        if form.is_valid():
            form.save()
            data = {
                "title" : "Update Data Sekolah Dasar di Serang",
                "heading" : "Update Data Sekolah Dasar di Serang",
                "form" : form,
                "id" : id,
                "books" : books,
                "pesan" : "Data Berhasil Diupdate",
        }
        return redirect("/sekolah/")

    else:
        form = FormSekolah(instance=books)
        data = {
            "title" : "Update Data Sekolah Dasar di Serang",
            "heading" : "Update Data Sekolah Dasar di Serang",
            "form" : form,
            "books" : books,
        }
        return render(request, "update_SD.html", data)
    

def delete_SD(request, delete_id):
    Sekolah.objects.filter(id = delete_id).delete()
    return redirect( "/sekolah/")

def Murid(request):
    books = murid.objects.all()
    data = {
        "title"   : "Daftar Jumlah Murid Sekolah Dasar di Serang",
        "judul" : "Daftar Jumlah Murid Sekolah Dasar di Serang",
        "books"   : books,
    }
    return render(request, "Murid.html", data)

def tambah_murid(request):
    if request.POST:
        form = Formmurid(request.POST)
        if form.is_valid():
            form.save()
            form = Formmurid()
            data = {
                "title" : "Tambah Jumlah Murid Sekolah Dasar di Serang",
                "judul" : "Tambah Jumlah Murid Sekolah Dasar di Serang",
                "form" : form,
                "pesan" : "Data Berhasil Ditambahkan",
            }
            return render(request, "tambah_murid.html", data)
    else:
        form = Formmurid()
        data = {
            "title" : "Tambah Jumlah Murid Sekolah Dasar di Serang",
            "judul" : "Tambah Jumlah Murid Sekolah Dasar di Serang",
            "form" : form,
        }
        return render(request, "tambah_murid.html", data)

def update_murid(request, id_books):
    books = murid.objects.get(id = id_books)
    if request.POST:
        form = Formmurid(request.POST, instance=books)
        if form.is_valid():
            form.save()
            data = {
                "title" : "Update Jumlah Murid Sekolah Dasar di Serang",
                "judul" : "Update Jumlah Murid Sekolah Dasar di Serang",
                "form" : form,
                "id" : id,
                "books" : books,
                "pesan" : "Data Berhasil Diupdate",
        }
        return redirect("/Murid/")

    else:
        form = Formmurid(instance=books)
        data = {
            "title" : "Update Jumlah Murid Sekolah Dasar di Serang",
            "judul" : "Update Jumlah Murid Sekolah Dasar di Serang",
            "form" : form,
            "books" : books,
        }
        return render(request, "update_murid.html", data)
    

def delete_murid(request, delete_id):
    murid.objects.filter(id = delete_id).delete()
    return redirect( "/Murid/")