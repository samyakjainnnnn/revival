from django.urls import path
from . import views


urlpatterns = [
    path('cat/<str:page>', views.get_page, name='page'),
    path('courses/<str:course>', views.courses, name='courses'),
    path('cat/<str:teachers>', views.teachers, name='teachers'),
    path('', views.home, name='home'),
    path('free/', views.free, name='free'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('teachers/about/', views.about, name='teachers-about'),  

]
