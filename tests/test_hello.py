"""
This module contains tests for the Hello World app.
"""
# The pytest library is already imported in the workflow file pytest.yml
# import pytest

def test_main_page(client):
    """
    Test the Hello World endpoint of the app.
    """
    response = client.get('/')
    assert response.data == b'Hello, World Ver1'
