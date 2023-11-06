from django.urls import path
from .views import face, contact

urlpatterns = [
    path('', face, name='face'),
    path('contact/', contact, name='contact')
]
