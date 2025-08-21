from typing import Any

def process_action(action: dict[str, Any]) -> str:
    """Return a msg based on action type"""
    try:
        match action:
            case {"type": "login", "user": str(user), "time": int(time)}:
                return f"User {user} logged in at timestamp {time}"
            case {"type": "logout", "user": str(user)}:
                return f"User {user} logged out"
            case {"type": "error", "code": int(code)}:
                return f"Error occurred with code {code}"
            case {"type": "invalid"}:
                raise ValueError(f"Invalid action format: {action}")
            case _:
                raise TypeError(f"Error processing action: {action}")
    except (KeyError, TypeError) as e:
        return f"{e}"
    except ValueError as e:
        return f"{e}"

def get_unique_users(actions: list[dict[str, Any]]) -> set[str]:
    """Return a set of user names from action data"""

    users: set[str] = set()
    for action in actions:
        try:
            if "user" in action and isinstance(action["user"], str):
                users.add(action["user"])
        except TypeError:
            continue
    return users


def summarize_actions(actions: list[dict[str, Any]]) -> dict[str, int]:
    """Counts occurrences of each action type"""

    summary: dict[str, int] = {"login": 0, "logout": 0, "error": 0, "invalid": 0}
    for action in actions:
        try:
            match action.get("type"):
                case "login":
                    summary["login"] += 1
                case "logout":
                    summary["logout"] += 1
                case "error":
                    summary["error"] += 1
                case _:
                    summary["invalid"] += 1
        except (TypeError, AttributeError):
            summary["invalid"] += 1
    return summary
