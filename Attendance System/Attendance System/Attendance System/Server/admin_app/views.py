from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Admin
from django.contrib import messages
from rest_framework import generics
from .serializers import AdminSerializer
from rest_framework.permissions import AllowAny

def admin_login(request):
    if request.method == "POST":
        identifier = request.POST.get('username_or_email')
        password = request.POST.get('password')
        try:
            admin = Admin.objects.get(username=identifier) or Admin.objects.get(email=identifier)
            if check_password(password, admin.password):
                request.session['admin_id'] = admin.id
                return redirect('admin_dashboard')
            else:
                messages.error(request, "Invalid password")
        except Admin.DoesNotExist:
            messages.error(request, "Admin does not exist")
    return render(request, 'login.html')


def admin_dashboard(request):
    if 'admin_id' not in request.session:
        return redirect('admin_login')
    return render(request, 'dashboard.html')



def register_admin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
        elif Admin.objects.filter(username=username).exists() or Admin.objects.filter(email=email).exists():
            messages.error(request, "Admin with these details already exists")
        else:
            hashed_password = make_password(password)
            Admin.objects.create(username=username, email=email, password=hashed_password)
            messages.success(request, "Admin registered successfully")
            return redirect('admin_dashboard')
    
    return render(request, 'register.html')


class AdminCreateView(generics.CreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [AllowAny]