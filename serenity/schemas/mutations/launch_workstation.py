import graphene

from ... import resolvers
from .common import ProcessResult

__all__ = [
    'LaunchWorkstation',
]


class LaunchWorkstation(graphene.Mutation):
    """
    Launch a workstation
    """
    class Arguments:
        image_id = graphene.ID(required=True)
        user = graphene.String(required=True)
        ip_address = graphene.String(required=True)

    Output = ProcessResult

    @staticmethod
    def mutate(root, info, image_id, user, ip_address):
        """
        :param None root:
        :param graphql.execution.base.ResolveInfo info:
        :param str image_id:
        :param str user:
        :param str ip_address:
        :rtype: ProcessResult
        """
        return resolvers.launch_workstations(image_id, user, ip_address)
