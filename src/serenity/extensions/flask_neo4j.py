import typing

from neo4j import Neo4jDriver, GraphDatabase, Session
from flask import Flask, current_app, _app_ctx_stack

__all__ = [
    'Neo4j',
]


class Neo4j:
    """
    Flask extension for Neo4j
    """
    def __init__(self, app: Flask = None):
        """
        :param app: an optional application to initialize
        """
        self.app = app

        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask):
        """
        Initialize the extension

        :param app: the application to initialize
        """
        app.config.setdefault('NEO4J_URL', 'bolt://0.0.0.0:7687')
        app.config.setdefault('NEO4J_USER', 'neo4j')
        app.config.setdefault('NEO4J_PSWD', '')

        self.app = app
        app.teardown_appcontext(self._teardown)

    @staticmethod
    def _teardown(exception: Exception) -> Exception:
        """
        Context teardown handler

        :param exception: an optional runtime error
        """
        ctx = _app_ctx_stack.top

        # if the application context has a driver, close it.
        if not hasattr(ctx, 'driver'):
            return exception

        ctx.driver.close()
        return exception

    @property
    def driver(self) -> typing.Union[Neo4jDriver, None]:
        """
        :getter: the current driver
        """
        ctx = _app_ctx_stack.top
        if ctx is None:
            return None

        if not hasattr(ctx, 'driver'):
            config = current_app.config
            ctx.driver = GraphDatabase.driver(
                uri=config['NEO4J_URL'],
                auth=(config['NEO4J_USER'], config['NEO4J_PSWD'])
            )

        return ctx.driver

    @property
    def session(self) -> Session:
        """
        :getter: a neo4j session
        """
        return self.driver.session()
