# Talk urls
from django.urls import path
from talk.views import *


urlpatterns = [
    path('', home),
    path('create_post/', create_post),
    path('delete_post/', delete_post),
    
]
