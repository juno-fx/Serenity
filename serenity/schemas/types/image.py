import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from ... import resolvers
from .workstation import Workstation

__all__ = [
    'WorkstationConnection',
    'Image',
]


class WorkstationConnection(relay.Connection):
    """
    Connect Workstations to Images
    """
    class Meta:
        node = Workstation


class Image(SQLAlchemyObjectType):
    """
    Machine image to be launched on a workstation
    """
    class Meta:
        interfaces = (relay.Node,)
        model = resolvers.ImageModel

    number_running = graphene.Int(
        description='How many of these images are currently running?'
    )

    workstations = relay.ConnectionField(
        WorkstationConnection,
        description="The workstations running this image"
    )

    @staticmethod
    def resolve_number_running(root, info):
        """
        How many workstations are currently running this image?

        :param Image root:
        :param graphql.execution.base.ResolveInfo info:
        :rtype: int
        """
        # TODO: Read name from Infinity, read number from openfaas
        return 0

    @staticmethod
    def resolve_workstations(root, info):
        """
        What workstations exist for this image?

        :param Image root:
        :param graphql.execution.base.ResolveInfo info:
        :rtype: Workstation
        """
        # TODO: Read from openfaas
        raise NotImplementedError
