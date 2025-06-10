from unittest.mock import Mock

import pytest

from src.data_loading.loader import get_user_by_id


def test_get_user_by_id_success():
    # Create a mock DB client
    mock_db = Mock()
    mock_db.fetch_user.return_value = {"id": 1, "name": "Alice"}

    # Call the function with the mock
    result = get_user_by_id(1, mock_db)

    # Assert the returned data is correct
    assert result["name"] == "Alice"
    mock_db.fetch_user.assert_called_once_with(1)


def test_get_user_by_id_not_found():
    # Mock DB returns None to simulate user not found
    mock_db = Mock()
    mock_db.fetch_user.return_value = None

    # Assert that it raises an error
    with pytest.raises(ValueError, match="User not found"):
        get_user_by_id(42, mock_db)

    mock_db.fetch_user.assert_called_once_with(42)
