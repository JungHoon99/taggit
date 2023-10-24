from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from taggit.models import Tag

from todos.models import Todo
from todos.serializers import TodoSerializer
# Create your views here.

class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):

        return super().create(request, *args, **kwargs)
    

class TodoTagViewSet(ModelViewSet):
    serializer_class = TodoSerializer

    def get_queryset(self):
        tag_name = self.kwargs['tags']

        queryset = Todo.objects.filter(tags__name=tag_name)

        return queryset
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        
        return Response(serializer.data)


Todo_listAPI = TodoViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

Tag_listAPI = TodoTagViewSet.as_view({
    'get':'list'
})