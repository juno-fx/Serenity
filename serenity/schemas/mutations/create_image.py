import uuid

import graphene

from ... import resolvers

__all__ = [
    'CreateImage'
]


class CreateImageInput(graphene.InputObjectType):
    """
    The input object for creating a user
    """
    label = graphene.String(required=True)
    icon = graphene.String()
    name = graphene.String(required=True)
    limit = graphene.Int()


class CreateImageSuccess(graphene.ObjectType):
    """
    The response for successfully creating a user
    """
    result = graphene.Field('serenity.schemas.Image')


class GeneralError(graphene.ObjectType):
    """
    Standard response for all errors
    """
    message = graphene.String(required=True)


class CreateImagePayload(graphene.Union):
    """
    Generic response for all user creation mutations
    """
    class Meta:
        types = (
            CreateImageSuccess,
            GeneralError
        )


class CreateImage(graphene.Mutation):
    class Arguments:
        input = CreateImageInput()

    Output = CreateImagePayload

    @staticmethod
    def mutate(root, info, input):
        session = info.context.get('session')

        try:
            image = resolvers.infinity.ImageModel(
                id=str(uuid.uuid4()),
                label=input.label,
                icon=input.icon,
                name=input.name,
                limit=input.limit
            )
            session.add(image)
            session.commit()
            return CreateImageSuccess(result=image)

        except Exception as e:
            return GeneralError(message=e)
