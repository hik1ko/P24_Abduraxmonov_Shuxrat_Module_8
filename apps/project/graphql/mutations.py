import graphene
from apps.project.graphql.mutates import create_project_mutation, update_project_mutation, delete_project_mutation, \
    update_task_mutation, update_comment_mutation
from apps.project.graphql.types import ProjectType, TaskType, CommentType


class CreateProject(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        description = graphene.String()
        assignees = graphene.List(graphene.String)

    project = graphene.Field(ProjectType)

    @classmethod
    def mutate(cls, info, name, description, assignees):
        project = create_project_mutation(name, description, assignees, author=info.context.user)
        return project

class UpdateProject(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        description = graphene.String()
        assignees = graphene.List(graphene.String)

    project = graphene.Field(ProjectType)

    @classmethod
    def mutate(cls, info, id, description, assignees):
        project = update_project_mutation(id, description, assignees)
        return UpdateProject(project=project)

class DeleteProject(graphene.Mutation):
    class Arguments:
        id = graphene.String()

    project = graphene.Field(ProjectType)

    @classmethod
    def mutate(cls, info, id):
        return delete_project_mutation(id)


class CreateTask(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        description = graphene.String()
        assignees = graphene.List(graphene.String)
        project = graphene.Int(graphene.ID, required=True)
        deadline = graphene.Date()

    task = graphene.Field(TaskType)

class UpdateTask(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        description = graphene.String()
        assignees = graphene.List(graphene.String)
        project = graphene.Int(graphene.ID, required=True)
        deadline = graphene.Date()

    task = graphene.Field(TaskType)

    @classmethod
    def mutate(cls, info, id, *kwargs):
        task = update_task_mutation(id=id, **kwargs)
        return UpdateTask(task=task)

class DeleteTask(graphene.Mutation):
    class Arguments:
        id = graphene.String()

    task = graphene.Field(TaskType)

    @classmethod
    def mutate(cls, info, id):
        return delete_project_mutation(id)


class CreateComment(graphene.Mutation):
    class Arguments:
        body = graphene.String()
        task = graphene.Int(graphene.ID, required=True)

    comment = graphene.Field(CommentType)

class UpdateComment(graphene.Mutation):
    class Arguments:
        body = graphene.String()
        task = graphene.Int(graphene.ID, required=True)
    comment = graphene.Field(CommentType)

    @classmethod
    def mutate(cls, info, id, task, body):
        comment = update_comment_mutation(id=id, task=task, body=body)
        return UpdateComment(comment=comment)

class DeleteComment(graphene.Mutation):
    class Arguments:
        id = graphene.String()

    comment = graphene.Field(CommentType)

    @classmethod
    def mutate(cls, info, id):
        return delete_project_mutation(id)



class Mutation(graphene.ObjectType):
    create_project = CreateProject.Field()
    update_project = UpdateProject.Field()
    delete_project = DeleteProject.Field()
    create_task = CreateTask.Field()
    update_task = UpdateTask.Field()
    delete_task = DeleteTask.Field()
    create_comment = CreateComment.Field()
    update_comment = UpdateComment.Field()
    delete_comment = DeleteComment.Field()
