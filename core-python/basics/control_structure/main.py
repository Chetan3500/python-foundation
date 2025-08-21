"""Control Structure"""

from typing import Any
from module.control_structure import process_action, get_unique_users, summarize_actions

def main() -> None:
    """Main entry point of the program"""

    actions: list[dict[str, Any]] = [
        {"type": "login", "user": "Alice", "time": 1001},
        {"type": "logout", "user": "Bob"},
        {"type": "error", "code": 404},
        {"type": "login", "user": "Alice", "time": 1002},
        {"type": "invalid"},  # Invalid action
        {"user": "Charlie"},  # Missing type
        None,  # Invalid type
    ]

    # Process individual actions
    print("Processing Actions:")
    for action in actions:
        result = process_action(action)
        print(result)

    # Get unique users
    unique_users = get_unique_users(actions)
    print(f"\nUnique Users: {unique_users}")

    # Summarize actions
    summary = summarize_actions(actions)
    print("\nAction Summary:")
    for action_type, count in summary.items():
        print(f"{action_type.capitalize()}: {count}")


if __name__ == "__main__":
    main()
