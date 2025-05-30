from django.urls import path
from .views import limited_view

urlpatterns = [
    path('limited/', limited_view, name='limited'),
]
