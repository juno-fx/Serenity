import graphene

from .. import mutations

__all__ = [
    'Mutate',
]


class Mutate(graphene.ObjectType):
    create_image = mutations.CreateImage.Field()
    launch_workstation = mutations.LaunchWorkstation.Field()
    shutdown_workstation = mutations.ShutdownWorkstation.Field()
