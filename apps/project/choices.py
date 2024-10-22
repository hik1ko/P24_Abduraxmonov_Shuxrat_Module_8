from django.db import models


class Status(models.TextChoices):
    PENDING = 'pending', 'Pending'
    ONGOING = 'ongoing', 'Ongoing'
    DONE = 'done', 'Done'


class NotificationType(models.TextChoices):
    PROJECT_STARTED = 'project_started', 'Project started'
    PROJECT_STOPPED = 'project_stopped', 'Project stopped'
    NEW_TASK = 'new_task', 'New task'
    TASK_UPDATE = 'task_update', 'Task update'
    OTHER = 'other', 'Other'
