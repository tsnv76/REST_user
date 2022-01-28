import graphene
from graphene_django import DjangoObjectType
from todoapp.models import Project, ToDo
from users.models import CustomUser


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class UsersType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = '__all__'


class TodoType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'


class Query(graphene.ObjectType):
    all_projects = graphene.List(ProjectType)

    def resolve_all_project(root, info):
        return Project.objects.all()

    all_todo = graphene.List(TodoType)

    def resolve_all_todo(root, info):
        return ToDo.objects.all()

    all_users = graphene.List(UsersType)

    def resolve_all_users(root, info):
        return CustomUser.objects.all()

    user_by_id = graphene.Field(UsersType, id=graphene.Int(required=True))

    def resolve_user_by_id(root, info, id):
        try:
            return CustomUser.objects.get(id=id)
        except CustomUser.DoesNotExist:
            return None

    project_by_name = graphene.List(ProjectType, name=graphene.String(required=False))

    def resolve_project_by_name(root, info, name):
        project = Project.objects.all()
        if name:
            project = project.filter(name=name)
        return project


# class ProjectCreateMutation(graphene.Mutation):
#     class Arguments:
#         name = graphene.String(required=True)
#         repo_link = graphene.String(required=True)
#
#     project = graphene.Field(ProjectType)
#
#     @classmethod
#     def mutate(cls, root, info, name, repo_link):
#         project = Project(name=name, repo_link=repo_link)
#         project.save()
#         return ProjectCreateMutation(project)
#
#
# class ProjectUpdateMutation(graphene.Mutation):
#     class Arguments:
#         id = graphene.Int(required=True)
#         name = graphene.String(required=False)
#         repo_link = graphene.String(required=False)
#
#     project= graphene.Field(ProjectType)
#
#     @classmethod
#     def mutate(cls, root, info, id, name=None, repo_link=None):
#         project = Project.objects.get(id=id)
#         if name:
#             project.name = name
#         if repo_link:
#             project.repo_link = repo_link
#         if name or repo_link:
#             project.save()
#         return ProjectUpdateMutation(project)
#
#
# class Mutations(graphene.ObjectType):
#     create_project = ProjectCreateMutation.Field()
#     update_project = ProjectUpdateMutation.Field()
#
#
# schema = graphene.Schema(query=Query, mutation=Mutations)
