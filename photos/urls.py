from django.urls import path
from photos import views


urlpatterns = [

    path('register/', views.registerPage, name="register"),    
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),

    path('', views.gallery, name="gallery"),
    
    path('add/', views.addPhoto, name="add"),
    path('photo/<str:pk>/', views.viewPhoto, name="photo"), 
 

]
