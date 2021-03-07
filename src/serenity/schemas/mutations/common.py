# pylint: disable=too-few-public-methods
import graphene

__all__ = [
    'GeneralError',
    'ProcessResult',
]


class ProcessResult(graphene.ObjectType):
    """
    Response from system processes
    """
    exit_code = graphene.Int(required=True)
    response = graphene.String()


class GeneralError(graphene.ObjectType):
    """
    Standard response for all errors
    """
    message = graphene.String(required=True)
