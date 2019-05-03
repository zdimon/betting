import graphene

from graphene_django.types import DjangoObjectType
from .models import Fixture

class FixtureType(DjangoObjectType):
    class Meta:
        model = Fixture

class Query(graphene.ObjectType):
    all_fixtures = graphene.List(FixtureType)
    def resolve_all_fixtures(self,info, **kwargs):
        return Fixture.objects.all()

schema = graphene.Schema(query=Query)