from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.get_notes),
    path('notes/create/', views.create_note),
    path('notes/update/<int:id>/', views.update_note),
]