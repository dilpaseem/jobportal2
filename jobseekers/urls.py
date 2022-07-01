from django.urls import path

from . import views
app_name='jbskr'
urlpatterns=[
path('login', views.user_login,name='login'),
path('jobsearch', views.search_job,name='jobsearch'),
path('jobdetails', views.details_job,name='jobdetails'),
]