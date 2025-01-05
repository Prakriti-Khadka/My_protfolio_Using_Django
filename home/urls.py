from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_title = "Prakriti Khadka"
admin.site.site_header = "Prakriti Khadka"
admin.site.index_title = "Welcome to Prakriti's Website"

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('', views.index, name='home'), 
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
]



