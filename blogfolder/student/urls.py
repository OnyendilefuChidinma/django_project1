from django.urls import path
from .home import HomepageView, view_profile
# from . import home


urlpatterns = [
    # path('', HomepageView.as_view(), name='homeview'),
    # path('', HomepageView.as_view(), name='dashboardView'),
    # path('student_dashboard/', HomepageView, name='dashboardView')
    # path('student_dashboard/', HomepageView.as_view(), name='dashboardView'),
    
    path('student_dashboard/', HomepageView.as_view(), name='dashboardView'),
    
    path('profile/<int:student_id>/', view_profile, name='student_profile')
    # path('student_dashboard/<int:student_id>/', view_profile, name='student_profile')

]
