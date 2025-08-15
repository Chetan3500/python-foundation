import pytest
from typing import Tuple, List
from basics.regex_tuples.main import extract_log_info, filter_logs, count_by_hour

def test_extract_log_info() -> None:
    """Test extracting IP and timestamp from log entries."""
    log = "192.168.1.1 [2025-08-14 11:49:00] GET /api"
    expected: Tuple[str, str] = ("192.168.1.1", "2025-08-14 11:49:00")
    assert extract_log_info(log) == expected, "Valid log should extract IP and timestamp"

    # Invalid log
    assert extract_log_info("invalid log entry") is None, "Invalid log should return None"
    
    # Malformed IP
    assert extract_log_info("999.999.999.999 [2025-08-14 11:49:00]") is None, "Malformed IP should return None"
    
    # None input
    assert extract_log_info(None) is None, "None input should return None"

def test_filter_logs() -> None:
    """Test filtering logs by IP prefix."""
    logs: List[str] = [
        "192.168.1.1 [2025-08-14 11:49:00] GET /api",
        "10.0.0.1 [2025-08-14 11:50:00] POST /login",
        "192.168.1.2 [2025-08-14 12:01:00] GET /data"
    ]
    expected: List[Tuple[str, str]] = [
        ("192.168.1.1", "2025-08-14 11:49:00"),
        ("192.168.1.2", "2025-08-14 12:01:00")
    ]
    assert filter_logs(logs, "192.168") == expected, "Should filter logs by IP prefix"

    # Empty list
    assert filter_logs([], "192.168") == [], "Empty list should return empty list"
    
    # No matching IPs
    assert filter_logs(logs, "172.16") == [], "No matching IPs should return empty list"

def test_count_by_hour() -> None:
    """Test counting logs by hour."""
    logs: List[Tuple[str, str]] = [
        ("192.168.1.1", "2025-08-14 11:49:00"),
        ("192.168.1.2", "2025-08-14 11:50:00"),
        ("192.168.1.3", "2025-08-14 12:01:00")
    ]
    expected: dict[str, int] = {
        "2025-08-14 11": 2,
        "2025-08-14 12": 1
    }
    assert count_by_hour(logs) == expected, "Should count logs by hour"

    # Empty list
    assert count_by_hour([]) == {}, "Empty list should return empty dict"

def test_count_by_hour_edge_cases() -> None:
    """Test edge cases for count_by_hour."""
    # Invalid tuple
    logs: List[Tuple[str, str]] = [
        ("192.168.1.1", "invalid-timestamp"),
        (None, None)  # type: ignore
    ]
    assert count_by_hour(logs) == {}, "Invalid timestamps should return empty dict"
