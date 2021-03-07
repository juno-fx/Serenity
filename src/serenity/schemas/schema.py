# pylint: disable=too-few-public-methods
import graphene
from graphene import relay

from . import types

__all__ = [
    'Query',
    'Mutate',
]


class Query(graphene.ObjectType):
    """
    The queries for Serenity
    """
    images = graphene.List(types.Image)
    workstations = graphene.List(types.Workstation)
    node = relay.Node.Field()

    @staticmethod
    def resolve_images(root, info):
        """
        :param Query root:
        :param graphql.execution.base.ResolveInfo info:
        """
        # TODO: Read from Infinity
        from ..resolvers import graph

        return graph.get_images()

    @staticmethod
    def resolve_workstations(root, info):
        """
        :param Query root:
        :param graphql.execution.base.ResolveInfo info:
        """
        # TODO: Read from openfaas
        raise NotImplementedError


class Mutate(graphene.ObjectType):
    """
    All mutations for Serenity
    """
