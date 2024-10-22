from apps.account.models import User
from apps.project.models import Project, Task, Comment


def create_project_mutation(name, description, assignees, author):
    author = User.objects.get(author)
    project = Project(name=name,
                      description=description,
                      assignees=assignees,
                      author=author)
    project.save()
    return project


def update_project_mutation(id, description, assignees):
    project = Project.objects.get_object_or_404(Project, pk=id)
    project.description = description
    project.assignees = assignees
    project.save()
    return project


def delete_project_mutation(id):
    project = Project.objects.get_object_or_404(Project, pk=id)
    project.delete()
    return True


def create_task_mutation(name, description, assignees, project, deadline):
    project = Project.objects.get_object_or_404(Project, pk=project)
    task = Task(name=name,
                description=description,
                assignees=assignees,
                project=project,
                deadline=deadline)
    task.save()
    return task


def update_task_mutation(id, **kwargs):
    task = Task.objects.get_object_or_404(Task, pk=id)
    project = kwargs.pop("project", None)
    for key, value in kwargs.items():
        setattr(task, key, value)
    if project:
        task.project = project
    task.save()
    return task


def delete_task_mutation(id):
    task = Task.objects.get_object_or_404(Task, pk=id)
    task.delete()
    return True


def create_comment_mutation(task, body):
    task = Task.objects.get_object_or_404(Task, pk=id)
    comment = Comment(task=task, body=body)
    comment.save()
    return comment


def update_comment_mutation(id, task, body):
    comment = Comment.objects.get_object_or_404(Comment, pk=id)
    comment.task = task
    comment.body = body
    comment.save()
    return comment


def delete_comment_mutation(id):
    comment = Comment.objects.get_object_or_404(Comment, pk=id)
    comment.delete()
    return True
