"""
All tables and data for the resources schema
"""
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

__all__ = [
    'BaseModel',
    'ImageModel',
]

# Common tables
BaseModel = declarative_base()

# Custom data types
# TODO: This should probably be an *actual* custom type, not just a string,
#  but it seems that graphene-sqlalchemy has trouble auto-mapping when we do that.
UUID = sqlalchemy.String(length=36)


class ImageModel(BaseModel):
    """

    """
    __tablename__ = 'images'

    id = sqlalchemy.Column(
        UUID,
        primary_key=True
    )

    label = sqlalchemy.Column(
        sqlalchemy.String,
        nullable=False,
        doc='A human friendly name for the image'
    )

    # TODO: Set the default icon path
    icon = sqlalchemy.Column(
        sqlalchemy.String,
        default='',
        doc='An icon associated with the image'
    )

    name = sqlalchemy.Column(
        sqlalchemy.String,
        doc='The name of the image that will load'
    )

    creation_date = sqlalchemy.Column(
        sqlalchemy.DateTime,
        server_default=sqlalchemy.sql.func.now(),
        doc='The creation date time of this image'
    )

    limit = sqlalchemy.Column(
        sqlalchemy.Integer,
        default=0,
        doc='The maximum number of these images allowed to be running simultaneously'
    )

    # workstations = relay.ConnectionField(
    #     WorkstationConnection, description="The workstations running this image"
    # )
