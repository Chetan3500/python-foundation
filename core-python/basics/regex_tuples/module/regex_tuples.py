import re
from typing import Tuple, List


def extract_log_info(log: str) -> Tuple[str, str] | None:
    """Return (IP, timestamp) tuple or None if invalid"""
    try:
        # Match IP (e.g., 192.168.1.1) and timestamp (e.g., 2025-08-14 11:49:00)
        pattern = r"((?:(?:25[0-5]|2[0-4]\d|1\d\d|\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d\d|\d?\d))\s+\[(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})\]"
        match = re.match(pattern, log)
        if match:
            return (match.group(1), match.group(2))
        return None
    except TypeError:
        return None


def filter_logs(logs: List[str], ip_prefix: str) -> List[Tuple[str, str]]:
    """Returns List of (IP, timestamp) tuples for matching IPs."""
    filtered: List[Tuple[str, str]] = []
    for log in logs:
        result = extract_log_info(log)
        if result and result[0].startswith(ip_prefix):
            filtered.append(result)
    return filtered


def count_by_hour(logs: List[Tuple[str, str]]) -> dict[str, int]:
    """Groups logs by hour and count occurrences"""
    counts: dict[str, int] = {}
    for ip, timestamp in logs:
        try:
            # Extract hour part (e.g., '2025-08-14 11' from '2025-08-14 11:49:00')
            pattern = r"(\d{4}-\d{2}-\d{2}\s+\d{2})"
            hour = timestamp[:13]
            if re.match(pattern, hour):
                counts[hour] = counts.get(hour, 0) + 1
        except (TypeError, ValueError):
            continue
    return counts
