from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name = 'home'),
    path('detail/<str:pk>/', views.detail, name= 'detail'),
    path('about/', views.about, name='about'),
    path('contactme/', views.contact, name='contact'),
    path('category/', views.ProjectListView.as_view(), name='list'),



]