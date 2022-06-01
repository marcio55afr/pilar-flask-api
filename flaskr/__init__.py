from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask('flaskr')
    
    if test_config is not None:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    from . import case
    app.register_blueprint(case.bp)
    
    return app