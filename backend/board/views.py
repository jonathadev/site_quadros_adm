from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer

@api_view(['GET'])
def list_notes(request):
    notes = Note.objects.all()
    return Response(NoteSerializer(notes, many=True).data)


@api_view(['POST'])
def create_note(request):
    serializer = NoteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['PUT'])
def update_note(request, id):
    note = Note.objects.get(id=id)
    serializer = NoteSerializer(note, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def delete_note(request, id):
    note = Note.objects.get(id=id)
    note.delete()
    return Response({"message": "Deleted"})


@api_view(['DELETE'])
def delete_all_notes(request):
    Note.objects.all().delete()
    return Response({"message": "Todas deletadas"})