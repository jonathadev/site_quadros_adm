from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Note

@api_view(['GET'])
def get_notes(request):
    notes = list(Note.objects.values())
    return Response(notes)

@api_view(['POST'])
def create_note(request):
    note = Note.objects.create(
        text=request.data.get('text'),
        x=request.data.get('x'),
        y=request.data.get('y'),
        color=request.data.get('color')
    )
    return Response({"id": note.id})

@api_view(['POST'])
def update_note(request, id):
    note = Note.objects.get(id=id)
    note.x = request.data.get('x')
    note.y = request.data.get('y')
    note.save()
    return Response({"status": "ok"})