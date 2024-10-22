from graphene_django import DjangoObjectType

from apps.account.models import User
from apps.project.models import Project, Task, Notification, Comment


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class TaskType(DjangoObjectType):
    class Meta:
        model = Task
        fields = '__all__'


class NotificationType(DjangoObjectType):
    class Meta:
        model = Notification
        fields = '__all__'

class CommentType(DjangoObjectType):
    class Meta:
        model = Comment
        fields = '__all__'


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'

