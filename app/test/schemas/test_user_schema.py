import pytest
from app.schemas.user import User


def test_user_schema():
    user = User(username="Paulo", password="pass#")

    assert user.dict() == {
        "username": "Paulo",
        "password": "pass#"
    }

def test_user_schema_invalid_username():
    with pytest.raises(ValueError):
        user = User(username="Paulo#", password="pass#")
