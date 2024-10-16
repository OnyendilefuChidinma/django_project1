from django.urls import path
from . import views


urlpatterns = [
    
    # path('', views.student_dashboard, name='student_dashboard')
    # path('students/', views.student_list, name='student_list')
    path('', views.student_list, name='student_list')
]
