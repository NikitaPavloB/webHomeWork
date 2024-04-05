import pytest
from conftest import auth_token

def test_auth_token(auth_token):
    assert auth_token is not None, "Failed to get auth token"
