from django.urls import path
from . import views

urlpatterns = [
    path('operators/<pk>/', views.OperatorView.as_view()),
    path('aircrafts/', views.AircraftListView.as_view()),
    path('aircraft/<pk>/', views.AircraftView.as_view()),
    path('locations/', views.AircraftLocationView.as_view()),
]