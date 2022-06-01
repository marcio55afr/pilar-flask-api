import pytest
from flaskr import create_app

@pytest.fixture
def client():
    """Configures the app for testing

    Sets app config variable ``TESTING`` to ``True``

    :return: App for testing
    """
    app = create_app()
    client = app.test_client()

    yield client