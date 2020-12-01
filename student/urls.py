from django.urls import path

from .views import home_page, about_page, student_page

urlpatterns = [
    path('', home_page, name= 'home'),
    path('home/', home_page, name= 'home'),
    path('about/', about_page, name= 'about'),
    path('student/', student_page, name= 'student'),
]