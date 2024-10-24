from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("graphql", GraphQLView.as_view(graphiql=True)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/account/v1/', include('apps.account.urls'))
]
