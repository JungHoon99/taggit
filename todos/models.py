from django.db import models
import uuid

from taggit.managers import TaggableManager
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase

# Create your models here.

class UUIDTaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):
    # If you only inherit GenericUUIDTaggedItemBase, you need to define
    # a tag field. e.g.
    #tag = models.ForeignKey(Tag, related_name="uuid_tagged_items", on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("tag")
        verbose_name_plural = ("tag")

class Todo(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(null=False, max_length=100)
    start_datetime = models.DateTimeField(null=False)
    end_datetime = models.DateTimeField(null=False)

    tags = TaggableManager(through=UUIDTaggedItem)
