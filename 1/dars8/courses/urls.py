from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('courses/<int:pk>/update/', views.update_course, name='update_course'),
    path('courses/<int:pk>/delete/', views.delete_course, name='delete_course'),
    path('lessons/<int:pk>/update/', views.update_lesson, name='update_lesson'),
    path('lessons/<int:pk>/delete/', views.delete_lesson, name='delete_lesson'),
]
