import factory

from apps.api.tests.factories import JobFactory
from ..models import Action


class ActionFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Action

    description = 'Description'
    connected_object_id = 1
    object_type = Action.ST

    @factory.post_generation
    def connected_users(self, create, extracted, **kwargs):
        if extracted:
            for user in extracted:
                self.connected_users.add(user)
