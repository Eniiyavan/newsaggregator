from django.urls import path
from . import views

urlpatterns=[
    path('',views.display_data),
    path('scrape/',views.scrape),
    path('specific_page/', views.specific_page, name='specific_page'),
   
]