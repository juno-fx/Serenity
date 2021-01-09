import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField

from .image import Image
from .workstation import Workstation

__all__ = [
    'Query',
]


class Query(graphene.ObjectType):
    """
    The main queries for Serenity
    """
    images = SQLAlchemyConnectionField(
        Image._meta.connection
    )
    workstations = graphene.List(Workstation)
    node = relay.Node.Field()

    # @staticmethod
    # def resolve_images(root, info):
    #     """
    #     :param Query root:
    #     :param graphql.execution.base.ResolveInfo info:
    #     """
    #     # TODO: Read from Infinity
    #     raise NotImplementedError

    @staticmethod
    def resolve_workstations(root, info):
        """
        :param Query root:
        :param graphql.execution.base.ResolveInfo info:
        """
        # TODO: Read from openfaas
        raise NotImplementedError
