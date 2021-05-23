import datetime
import click
from flask.cli import with_appcontext
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship, backref
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    db.drop_all()
    db.create_all()
    click.echo('Initialized the database.')


class Users(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    dt_created = Column(DateTime, default=datetime.datetime.now())


class Departments(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    dt_created = Column(DateTime, default=datetime.datetime.now())
    parent_id = Column(Integer, ForeignKey('Departments.id'), nullable=True)
    director_id = ForeignKey('Users.id')

    chils_departments = relationship('Departments', cascade='all',
        backref=backref('parent_department', remote_side='Departments.id', lazy='joined'), 
        lazy='dynamic')
    director = relationship('Users', lazy='joined')


class Roles(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)


class UserRoles(db.Model):
    id = Column(Integer, primary_key=True)
    role_id = ForeignKey('Roles.id')
    user_id = ForeignKey('Users.id')
    dts = Column(DateTime, default=datetime.datetime.now())
    dte = Column(DateTime, nullable=True)
