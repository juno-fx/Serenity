import logging
import os

import dotenv
import graphene
import sqlalchemy.orm
from flask import Flask
from flask_graphql import GraphQLView

from . import schemas

__all__ = [
    'create_app',
]


dotenv.load_dotenv()
logging.basicConfig()

LOG = logging.getLogger(__name__)
CONNECTION_STRING = 'postgresql://{user}:{pwd}@db:5432'.format(
    user=os.environ['POSTGRES_USER'],
    pwd=os.environ['POSTGRES_PASSWORD']
)
SESSION = sqlalchemy.orm.scoped_session(
    sqlalchemy.orm.sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=sqlalchemy.create_engine(CONNECTION_STRING)
    )
)


def create_app(name='serenity'):
    """
    Create a Serenity Flask app with the given name

    :param str name: The name of the application
    :rtype: Flask
    """
    debug = bool(os.environ.get('DEV'))
    schema = graphene.Schema(query=schemas.Query, mutation=schemas.Mutate)

    app = Flask(name)
    app.root_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    app.debug = debug
    logging.root.setLevel(logging.WARNING if not debug else logging.DEBUG)

    # Setup graphql
    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True,
            middleware=[],
            get_context=lambda: {
                'session': SESSION
            }
        )
    )

    return app
