import graphene
from graphene import relay

__all__ = [
    'Workstation',
]


class Workstation(graphene.ObjectType):
    """
    An individual workstation, set up and registered to a single user
    """
    class Meta:
        interfaces = (relay.Node, )

    name = graphene.String()
    user = graphene.String()
    ip_address = graphene.String()
    uptime = graphene.Time()

    image = graphene.Field('serenity.schemas.Image')

    @classmethod
    def get_node(cls, info, id_):
        """
        :param str id_:
        :param graphql.execution.base.ResolveInfo info:
        """
        # TODO: Read from openfaas
        raise NotImplementedError

    @staticmethod
    def resolve_name(root, info):
        """
        Get the name for this workstation

        :param Workstation root:
        :param graphql.execution.base.ResolveInfo info:
        :rtype: str
        """
        # TODO: Read from openfaas
        raise NotImplementedError

    @staticmethod
    def resolve_user(root, info):
        """
        Get the user registered with this workstation

        :param Workstation root:
        :param graphql.execution.base.ResolveInfo info:
        :rtype: str
        """
        # TODO: Read from openfaas
        raise NotImplementedError

    @staticmethod
    def resolve_ip_address(root, info):
        """
        Get the IP address that is registered with this workstation

        :param Workstation root:
        :param graphql.execution.base.ResolveInfo info:
        :rtype: str
        """
        # TODO: Read from openfaas
        raise NotImplementedError

    @staticmethod
    def resolve_uptime(root, info):
        """
        How long has this workstation been running?

        :param Workstation root:
        :param graphql.execution.base.ResolveInfo info:
        :rtype: datetime.time
        """
        # TODO: Read from openfaas
        raise NotImplementedError

    @staticmethod
    def resolve_image(root, info):
        """
        Get the image this workstation is using

        :param Workstation root:
        :param graphql.execution.base.ResolveInfo info:
        :rtype: serenity.schemas.Image
        """
        # TODO: Read from openfaas
        raise NotImplementedError
