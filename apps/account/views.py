from rest_framework.viewsets import ModelViewSet

from apps.account.models import User
from apps.account.serializers import UserSerializer


class UserView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
