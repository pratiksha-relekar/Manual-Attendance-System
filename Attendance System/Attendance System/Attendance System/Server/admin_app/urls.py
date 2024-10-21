from django.urls import path
from admin_app.views import *

urlpatterns = [
    path('', admin_login, name='admin_login'),
    path('dashboard/', admin_dashboard, name='admin_dashboard'),
    path('register/', register_admin, name='register_admin'),
    path('api/admin/', AdminCreateView.as_view(), name='admin-create'),
]
