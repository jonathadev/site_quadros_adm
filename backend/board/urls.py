from django.urls import path
from .views import NoteList, NoteCreate, NoteUpdate, NoteDelete

urlpatterns = [
    path('notes/', NoteList.as_view(), name='note-list'),
    path('notes/create/', NoteCreate.as_view(), name='note-create'),
    path('notes/update/<int:id>/', NoteUpdate.as_view(), name='note-update'),
    path('notes/delete/<int:id>/', NoteDelete.as_view(), name='note-delete'),
    
]