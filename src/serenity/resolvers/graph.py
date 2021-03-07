from flask import Flask

from .. import extensions
from .. import schemas

__all__ = [
    'init_app',
]


DB = extensions.Neo4j()


def get_images():
    cypher = DB.session.run('MATCH (image:Image)')
    result = []
    for image_data in cypher:
        result.append(
            schemas.Image(
                whatever=image_data.something
            )
        )
    return result


def init_app(app: Flask):
    """
    Initialize the graph database to the given application

    :param flask.Flask app:
    """
    DB.init_app(app)
