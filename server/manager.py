#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# find . -name "*.pyc" -exec rm -rf {} \;

# python imports
import re

# flask imports
from flask_script import Manager

# project imports
from application import create_app
from application.config import DefaultConfig


app = create_app(DefaultConfig)
manager = Manager(app)


@manager.command
def jsons():
    """
    Generate json files from Json classes
    """

    # python imports
    from json import dump
    import pkgutil
    import inspect
    import os

    # project imports
    from application import jsons

    def uncamelize(camel):
        return re.sub('(.)([A-Z]{1})', r'\1_\2', camel).lower()

    prefix = jsons.__name__ + "."
    for importer, modname, ispkg in pkgutil.iter_modules(jsons.__path__, prefix):

        module = __import__(modname, fromlist="dummy")
        members = inspect.getmembers(module, inspect.isclass)
        classes = [m[1] for m in members if m[1].__module__ == module.__name__]

        for model in classes:
            file_path = os.path.join(app.config['JSONSCHEMA_DIR'],
                                     '%s.json' % uncamelize(model.__name__))
            with open(file_path, 'w') as f:
                dump(model.get_schema(ordered=True), f)


@manager.command
def doc():
    """
    Generate documentation files
    """
    import subprocess
    subprocess.call("apidoc -i . -o ../doc/", shell=True)


@manager.command
def admin(reset=False):
    """
    If the account exists, reset its password and permissions
    """
    from application.models import Admin
    Admin.create_first_user(reset)


@manager.command
def init():
    """
    Initialize application setup
    """
    doc()
    jsons()
    admin()


@manager.command
def setup():
    """
    Production setup
    """
    admin()


@manager.command
def run(port=8080, setup=False):
    """
    Run server in development mode
    """
    if setup:
        init()

    app.run(host='0.0.0.0', port=port, debug=True)


@manager.command
def test():
    """
    Run postman tests

    NOTE: SITE_NAME var in config should match postman file names
    """
    import sys
    import subprocess
    import os

    app_name = app.config['SITE_NAME']
    postman_dir = os.path.join(sys.path[0], '../postman')
    os.chdir(postman_dir)

    collection = '{}.postman_collection.json'.format(app_name)
    environment = '{}.postman_environment.json'.format(app_name)

    subprocess.call("newman run {} -e {}".format(collection, environment), shell=True)


if __name__ == '__main__':
    manager.run()
