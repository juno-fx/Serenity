import graphene

__all__ = [
    'ProcessResult',
]


class ProcessResult(graphene.ObjectType):
    """
    Result object from system processes
    """
    exit_code = graphene.Int(description='', required=True)
    response = graphene.String()
