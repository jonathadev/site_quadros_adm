from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.list_notes),
    path('notes/create/', views.create_note),
    path('notes/update/<int:id>/', views.update_note),
    path('notes/delete/<int:id>/', views.delete_note),
    path('notes/delete-all/', views.delete_all_notes),
]