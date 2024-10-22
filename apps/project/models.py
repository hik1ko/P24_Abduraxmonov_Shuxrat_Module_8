from django.db import models

from apps.account.models import User
from apps.project.choices import Status


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Project(TimeStamp):
    name = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    assignees = models.ManyToManyField(User)

    class Meta:
        ordering = ['updated_at']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name


class Task(TimeStamp):
    name = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    status = models.CharField(max_length=100, choices=Status.choices, default=Status.PENDING)
    deadline = models.DateTimeField()
    assignees = models.ManyToManyField(User)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ['updated_at']

    def __str__(self):
        return self.name

class Comment(TimeStamp):
    body = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['updated_at']

    def __str__(self):
        return self.body

class Notification(TimeStamp):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    type = models.CharField(max_length=100, choices=Status.choices)
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'
        ordering = ['updated_at']

    def mark_as_read(self):
        self.is_read = True
        self.save()

    def __str__(self):
        return self.message


