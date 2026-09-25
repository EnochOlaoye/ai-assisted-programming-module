"""A deliberately minimal email address validator."""

from __future__ import annotations


def is_valid_email(address: str) -> bool:
    """Return whether *address* has an ``@`` and a dot after it."""
    if not isinstance(address, str) or len(address) > 254:
        return False

    at = address.find("@")
    return at != -1 and "." in address[at + 1:]
