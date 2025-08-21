"""Regex Tuple"""

from typing import List
from module.regex_tuples import extract_log_info, filter_logs, count_by_hour

def main() -> None:
    """Main function to demonstrate log extraction and filtering"""
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
