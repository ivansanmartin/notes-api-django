from rest_framework import  serializers
from .models import Note


class NoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'title', 'body_text', 'created_date')
        read_only_fields = ('created_date',)
