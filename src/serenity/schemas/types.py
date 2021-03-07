# pylint: disable=missing-class-docstring, too-few-public-methods
import datetime
import typing

import graphql
import graphene
from graphene import relay

__all__ = [
    'Image',
    'Workstation',
]


class Workstation(graphene.ObjectType):
    """
    An individual workstation, set up and registered to a single user
    """
    class Meta:
        interfaces = (relay.Node, )

    name = graphene.String(
        description='The name of this workstation',
    )
    user = graphene.String(
        description='The user assigned to this workstation',
    )
    ip_address = graphene.String(
        description='The workstation\'s IP address',
    )
    uptime = graphene.Time(
        description='How long this workstation has been running',
    )

    image = graphene.Field(
        lambda: Image,
        description='The image being run on this workstation',
    )

    @classmethod
    def get_node(cls, info: graphql.ResolveInfo, id: str) -> 'Workstation':
        """
        :param info: meta information about the current query
        :param id: the global relay id to lookup
        :return: the name of this workstation
        """
        # pylint: disable=redefined-builtin, invalid-name
        # TODO: Read from openfaas
        raise NotImplementedError

    @staticmethod
    def resolve_name(parent: 'Workstation', info: graphql.ResolveInfo) -> str:
        """
        :param parent: object from the resolver of the parent field
        :param info: meta information about the current query
        :return: the name of this workstation
        """
        # TODO: Read from openfaas
        raise NotImplementedError

    @staticmethod
    def resolve_user(parent: 'Workstation', info: graphql.ResolveInfo) -> str:
        """
        :param parent: object from the resolver of the parent field
        :param info: meta information about the current query
        :return: the user registered to this workstation
        """
        # TODO: Read from openfaas
        raise NotImplementedError

    @staticmethod
    def resolve_ip_address(parent: 'Workstation', info: graphql.ResolveInfo) -> str:
        """
        :param parent: object from the resolver of the parent field
        :param info: meta information about the current query
        :return: the IP address of this workstation
        """
        # TODO: Read from openfaas
        raise NotImplementedError

    @staticmethod
    def resolve_uptime(parent: 'Workstation', info: graphql.ResolveInfo) -> datetime.time:
        """
        :param parent: object from the resolver of the parent field
        :param info: meta information about the current query
        :return: how long has this workstation been running?
        """
        # TODO: Read from openfaas
        raise NotImplementedError

    @staticmethod
    def resolve_image(parent: 'Workstation', info: graphql.ResolveInfo) -> 'Image':
        """
        :param parent: object from the resolver of the parent field
        :param info: meta information about the current query
        :return: the image this workstation is running
        """
        # TODO: Read from openfaas
        raise NotImplementedError


class WorkstationConnection(relay.Connection):
    """
    Connect Workstations to Images
    """
    class Meta:
        node = Workstation


class Image(graphene.ObjectType):
    """
    Machine image to be launched on a workstation
    """
    class Meta:
        interfaces = (relay.Node,)

    number_running = graphene.Int(
        description='How many workstations are currently running this image?'
    )

    workstations = relay.ConnectionField(
        WorkstationConnection,
        description="The workstations running this image"
    )

    @staticmethod
    def resolve_number_running(parent: 'Image', info: graphql.ResolveInfo) -> int:
        """
        :param parent: object from the resolver of the parent field
        :param info: meta information about the current query
        :return: how many workstations are running this image?
        """
        # TODO: Read name from Infinity, read number from openfaas
        raise NotImplementedError

    @staticmethod
    def resolve_workstations(parent: 'Image', info: graphql.ResolveInfo) -> typing.List[Workstation]:
        """
        :param parent: object from the resolver of the parent field
        :param info: meta information about the current query
        :return: the workstations running this image
        """
        # TODO: Read from openfaas
        raise NotImplementedError
