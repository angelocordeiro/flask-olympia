import click
from mr.ext.database import db
from mr.ext.auth import create_user
from mr.models import Mrdata


def create_db():
    """Cria o banco de dados"""
    db.create_all()


def drop_db():
    """Limpa o banco de dados"""
    db.drop_all()


def init_app(app):
    # for command in [create_db, drop_db, populate_db]:
    for command in [create_db, drop_db]:
        app.cli.add_command(app.cli.command()(command))

    # add a single command
    @app.cli.command()
    @click.option('--username', '-u')
    @click.option('--password', '-p')
    def add_user(username, password):
        """Adiciona um novo usuario no banco de dados"""
        return create_user(username, password)
