import pytest
from flaskr import create_app


@pytest.fixture
def app():
    app = create_app({
        'TESTING': True,
    })
    
    yield app

@pytest.fixture
def client(app):
    """Configures the app for testing

    Sets app config variable ``TESTING`` to ``True``

    :return: App for testing
    """
    client = app.test_client()
    yield client