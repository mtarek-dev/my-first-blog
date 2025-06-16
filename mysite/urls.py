from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from blog import views as v


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', v.logout_view, name='logout'),
    path('', include('blog.urls')),
]