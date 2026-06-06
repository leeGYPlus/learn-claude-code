"""hello.py – A simple greeting module.

This module provides a reusable greeting function and a CLI entry point.
"""


def greet(name: str) -> str:
    """Return a greeting message for the given name.

    Args:
        name: The name of the person to greet.

    Returns:
        A greeting string, e.g. ``"Hello, Claude"``.
    """
    return f"Hello, {name}"


def main() -> None:
    """Entry point: print a greeting to the console."""
    message: str = greet("Claude")
    print(message)


if __name__ == "__main__":
    main()
