from django.urls import path
from .views import production_counter 

urlpatterns = [
    path('production_counter/', production_counter, name = 'production_counter'),
]
