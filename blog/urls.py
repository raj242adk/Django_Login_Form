from django.urls import path
from . import views


urlpatterns = [
    path("",views.starting_page),
    path("posts/",views.post),
    path("posts/<slug:slug>",views.further_details)
    
    
]
