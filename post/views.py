from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Snack
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
class PostsList(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Snack.objects.all()
    serializer_class = PostSerializer

class PostsDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Snack.objects.all()
    serializer_class = PostSerializer
