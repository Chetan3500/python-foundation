"""Test cases for control structures"""

from typing import Any
import pytest
from module.control_structure import (
    process_action,
    get_unique_users,
    summarize_actions,
)


def test_process_action() -> None:
    """Test processing of different action types."""
    # Valid login action
    login_action: dict[str, Any] = {"type": "login", "user": "Alice", "time": 1001}
    assert (
        process_action(login_action) == "User Alice logged in at timestamp 1001"
    ), "Login action should return correct message"

    # Valid logout action
    logout_action: dict[str, Any] = {"type": "logout", "user": "Bob"}
    assert (
        process_action(logout_action) == "User Bob logged out"
    ), "Logout action should return correct message"

    # Valid error action
    error_action: dict[str, Any] = {"type": "error", "code": 404}
    assert (
        process_action(error_action) == "Error occurred with code 404"
    ), "Error action should return correct message"

    # Invalid action
    invalid_action: dict[str, Any] = {"type": "invalid"}
    assert "Invalid action format" in process_action(
        invalid_action
    ), "Invalid action should raise ValueError"


def test_process_action_edge_cases() -> None:
    """Test edge cases for process_action."""
    # Missing type
    no_type: dict[str, Any] = {"user": "Charlie"}
    assert "Error processing action" in process_action(
        no_type
    ), "Missing type should return error"

    # None action
    assert "Error processing action" in process_action(
        None
    ), "None action should return error"

    # Wrong type for time
    wrong_time: dict[str, Any] = {"type": "login", "user": "Alice", "time": "1001"}
    assert "Error processing action" in process_action(
        wrong_time
    ), "Invalid time type should return error"


def test_get_unique_users() -> None:
    """Test extraction of unique users from actions."""
    actions: list[dict[str, Any]] = [
        {"type": "login", "user": "Alice", "time": 1001},
        {"type": "logout", "user": "Bob"},
        {"type": "login", "user": "Alice", "time": 1002},
        {"type": "error", "code": 404},  # No user
        {"type": "logout", "user": "Charlie"},
    ]
    expected: set[str] = {"Alice", "Bob", "Charlie"}
    assert get_unique_users(actions) == expected, "Should return unique users"

    # Empty list
    assert get_unique_users([]) == set(), "Empty list should return empty set"


def test_get_unique_users_edge_cases() -> None:
    """Test edge cases for get_unique_users."""
    actions: list[dict[str, Any]] = [
        {"type": "login", "user": None},  # Invalid user
        None,  # Invalid action
        {"type": "error"},  # No user
    ]
    assert get_unique_users(actions) == set(), "Invalid users should return empty set"


def test_summarize_actions() -> None:
    """Test summarization of actions by type."""
    actions: list[dict[str, Any]] = [
        {"type": "login", "user": "Alice", "time": 1001},
        {"type": "logout", "user": "Bob"},
        {"type": "error", "code": 404},
        {"type": "login", "user": "Alice", "time": 1002},
        {"type": "invalid"},
        {"user": "Charlie"},
        None,
    ]
    expected: dict[str, int] = {"login": 2, "logout": 1, "error": 1, "invalid": 3}
    assert summarize_actions(actions) == expected, "Should count actions correctly"

    # Empty list
    expected_empty: dict[str, int] = {"login": 0, "logout": 0, "error": 0, "invalid": 0}
    assert (
        summarize_actions([]) == expected_empty
    ), "Empty list should return zero counts"


def test_summarize_actions_edge_cases() -> None:
    """Test edge cases for summarize_actions."""
    actions: list[dict[str, Any]] = [{"type": None}, None, {}]
    expected: dict[str, int] = {"login": 0, "logout": 0, "error": 0, "invalid": 3}
    assert (
        summarize_actions(actions) == expected
    ), "Invalid types should count as invalid"
