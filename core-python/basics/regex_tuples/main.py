"""Regex Tuple"""

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


def main() -> None:
    # Sample log entries
    logs: List[str] = [
        "192.168.1.1 [2025-08-14 11:49:00] GET /api",
        "10.0.0.1 [2025-08-14 11:50:00] POST /login",
        "192.168.1.2 [2025-08-14 12:01:00] GET /data",
        "invalid log entry",
        "192.168.1.3 [2025-08-14 11:55:00] GET /api",
        None,
    ]

    # Extract and print log info
    print("Extract Log Info:")
    for log in logs:
        result = extract_log_info(log)
        print(f"Log: {log} -> {result}")

    # Filter logs by IP Prefix
    ip_prefix: str = "192.168"
    filtered_logs = filter_logs(logs, ip_prefix)
    print(f"\nFiltered Logs (IP prefix: '{ip_prefix}'):")
    for ip, timestamp in filtered_logs:
        print(f"IP: {ip}, Timestamp: {timestamp}")

    # Count logs by hour
    counts = count_by_hour(filtered_logs)
    print("\nLog Counts by Hour:")
    for hour, count in counts.items():
        print(f"{hour}: {count} logs")


if __name__ == "__main__":
    main()
