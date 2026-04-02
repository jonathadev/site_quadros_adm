from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Note

from rest_framework import generics
from .serializers import NoteSerializer


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


# Listar todas as notas
class NoteList(generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

# Criar nova nota
class NoteCreate(generics.CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

# Atualizar nota (posição ou texto)
class NoteUpdate(generics.UpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = 'id'

# Deletar nota
class NoteDelete(generics.DestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = 'id'