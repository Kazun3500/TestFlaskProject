from datetime import datetime
import click
from flask.cli import with_appcontext
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    db.drop_all()
    db.create_all()
    click.echo('Initialized the database.')


class User(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    dt_created = Column(DateTime, default=datetime.now())

    def __repr__(self):
        return '<User %r>' % self.username