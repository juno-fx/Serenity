from flask import Flask

from .resolvers import graph


def create_image():
    """
    Create a new image in the connected database
    """
    graph.DB.session.run()


def drop_all():
    """
    Drop the connected database
    """


def init_app(app: Flask):
    """
    Add custom commands to the given application

    :param app: The application to initialize
    """
    app.cli.add_command(app.cli.command()(create_image))
    app.cli.add_command(app.cli.command()(drop_all))
