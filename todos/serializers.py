from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)
from rest_framework import serializers, exceptions

from todos.models import Todo


class TodoSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    def create(self, validated_data):
        to_be_tagged, validated_data = self._pop_tags(validated_data)
        
        tag_object = super(TaggitSerializer, self).create(validated_data)
        self._save_tags(tag_object, to_be_tagged)
        return tag_object

    class Meta:
        model=Todo
        fields=['title', 'tags', 'start_datetime', 'end_datetime']