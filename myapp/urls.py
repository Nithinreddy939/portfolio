from django.urls import path  
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='home'),
    path('projects/', views.projects, name='projects'),
    path('certifications/', views.certifications, name='certifications'),
    path('about/', views.about, name='about'),

    #login details
    path('login/', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),

    #searching the data
    # path('search/',views.search,name='search')
]
