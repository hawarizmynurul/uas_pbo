from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from SD.models import *

class FormSekolah(ModelForm):
    class Meta:
        model = Sekolah
        fields = '__all__'

        widgets = {
            'nama_sekolah' : forms.TextInput({'class':'form-control', 'placeholder':'Nama Sekolah', 'required':'required'}),
            'titik_koordinat' : forms.TextInput({'class':'form-control', 'placeholder':'Titik Koordinat Sekolah', 'required':'required'}),
            'keterangan' : forms.TextInput({'class':'form-control', 'placeholder':'Keterangan', 'required':'required'}),
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class Formmurid(ModelForm):
    class Meta:
        model = murid
        fields = '__all__'

        widgets = {
            'NPSN' : forms.TextInput({'class':'form-control', 'placeholder':'NPSN', 'required':'required'}),
            'nama' : forms.TextInput({'class':'form-control', 'placeholder':'Nama Sekolah', 'required':'required'}),
            'jmlhmurid' : forms.TextInput({'class':'form-control', 'placeholder':'Jumlah Murid', 'required':'required'}),
        }
    