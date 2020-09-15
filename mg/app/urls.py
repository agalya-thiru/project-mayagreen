from django.urls import path
from . import views

urlpatterns=[
    # path('',views.home,name="home"),
    path('',views.details,name="details"),
    path('next/',views.next,name="next"),
    # path('role/',views.role,name="role"),    
    # path('next/',views.next,name="next"),
   
]