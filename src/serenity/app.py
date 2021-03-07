import logging
import os

import graphene
from flask import Flask
from flask_graphql import GraphQLView

from . import commands
from . import schemas
from .resolvers import graph

__all__ = [
    'create_app',
]


logging.basicConfig()  # TODO: Configure the logger

LOG = logging.getLogger(__name__)


def create_app() -> Flask:
    """
    Create a Serenity Flask app with the given name
    """
    # TODO: Figure out Flask log handlers
    logging.root.setLevel(int(os.environ.get('LOG_LEVEL', logging.WARNING)))

    # Setup the app
    app = Flask('Serenity')
    app.config.from_mapping(
        NEO4J_URL=os.environ.get('NEO4J_URL'),
        NEO4J_USER=os.environ.get('NEO4J_USER'),
        NEO4J_PSWD=os.environ.get('NEO4J_PSWD'),
    )

    # Register extensions
    commands.init_app(app)
    graph.init_app(app)

    # GraphQL
    schema = graphene.Schema(query=schemas.Query)
    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True,
            middleware=[],
        )
    )

    return app
