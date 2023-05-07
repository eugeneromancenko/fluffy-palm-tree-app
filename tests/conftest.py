"""
This module defines fixtures and configuration for tests.
"""

import pytest

from hello import create_app

@pytest.fixture
def app():
    """
    Create an instance of the Hello World app for testing.
    """
    app = create_app()
    yield app

@pytest.fixture
def client(app):
    """
    Create a test client for the Hello World app..
    """
    test_client = app.test_client()
    return test_client
