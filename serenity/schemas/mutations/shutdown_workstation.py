import graphene

from .common import ProcessResult

__all__ = [
    'ShutdownWorkstation',
]


class ShutdownWorkstation(graphene.Mutation):
    """
    Shutdown a workstation
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
        result = ProcessResult()
        try:
            # TODO: Lookup workstation from Infinity, shutdown with openfaas
            raise NotImplementedError

            result.exit_code = 0
            result.message = '<<label>> shutdown successfully!'

        except Exception as exc:
            result.exit_code = -1
            result.message = f'<<label>> failed to shutdown:\n{exc}'

        return result
