from rest_framework import viewsets
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.contrib import messages
import requests

from .models import User, Customer, AdminProfile
from .serializers import UserSerializer, CustomerSerializer, AdminProfileSerializer
from .forms import UserRegisterForm, UserLoginForm


# API REST ViewSets
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class AdminProfileViewSet(viewsets.ModelViewSet):
    queryset = AdminProfile.objects.all()
    serializer_class = AdminProfileSerializer


# HTML Form View (registro clásico)
class UserRegisterView(FormView):
    template_name = 'users/register_form.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('user_register_form')

    def form_valid(self, form):
        api_url = 'http://localhost:8000/api/users/users/'  # URL de tu endpoint API DRF
        data = {
            "username": form.cleaned_data['username'],
            "email": form.cleaned_data['email'],
            "name": form.cleaned_data['name'],
            "password": form.cleaned_data['password'],
            "customer": {
                "processor": form.cleaned_data['processor'],
                "ram_gb": form.cleaned_data['ram_gb'],
                "graphics_card": form.cleaned_data['graphics_card']
            }
        }

        try:
            response = requests.post(api_url, json=data)
            if response.status_code == 201:
                messages.success(self.request, "Usuario registrado exitosamente.")
            else:
                error = response.json()
                messages.error(self.request, f"Error: {error}")
        except Exception as e:
            messages.error(self.request, f"Error al conectar con API: {str(e)}")

        return super().form_valid(form)
    

class UserLoginView(FormView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('user_register_form')  # O tu vista de inicio para clientes

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(self.request, username=username, password=password)

        if user is not None:
            login(self.request, user)
            messages.success(self.request, f"Bienvenido {user.username}")
            return super().form_valid(form)
        else:
            messages.error(self.request, "Credenciales inválidas. Inténtalo de nuevo.")
            return self.form_invalid(form)
