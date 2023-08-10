from .models import Note
from rest_framework import viewsets, permissions
from .serializers import NoteSerializers

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = NoteSerializers