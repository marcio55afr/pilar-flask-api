import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask('flaskr', instance_relative_config=True)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app