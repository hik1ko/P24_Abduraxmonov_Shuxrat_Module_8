from django.shortcuts import get_object_or_404

from apps.account.models import User
from apps.project.models import Notification, Project, Task, Comment


def resolve_all_notifications():
    queryset = Notification.objects.all()
    return queryset

def resolve_all_users():
    queryset = User.objects.all()
    return queryset

def resolve_all_projects():
    queryset = Project.objects.all()
    return queryset

def resolve_all_tasks():
    queryset = Task.objects.all()
    return queryset

def resolve_all_comments():
    queryset = Comment.objects.all()
    return queryset

def resolve_task(id):
    obj = get_object_or_404(Task, pk=id)
    return obj

def resolve_project(id):
    obj = get_object_or_404(Project, pk=id)
    return obj

def resolve_notification(id):
    obj = get_object_or_404(Notification, pk=id)
    return obj

def resolve_comment(id):
    obj = get_object_or_404(Comment, pk=id)
    return obj
