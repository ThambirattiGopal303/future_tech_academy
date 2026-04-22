from backend.views import index_page
from django.urls import path
urlpatterns = [
        path('index',index_page,name="index")
   
]
