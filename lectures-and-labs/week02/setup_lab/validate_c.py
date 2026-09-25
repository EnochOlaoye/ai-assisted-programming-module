"""A small email validator with explicit, readable checks."""

from __future__ import annotations


def is_valid_email(address: str) -> bool:
    """Return whether *address* has a simple conventional email shape."""
    if not isinstance(address, str) or len(address) > 254:
        return False
    if address != address.strip() or any(char.isspace() for char in address):
        return False

    local, separator, domain = address.partition("@")
    if not separator or "@" in domain or not local or not domain:
        return False
    if local.startswith(".") or local.endswith(".") or ".." in local:
        return False

    labels = domain.split(".")
    return len(labels) >= 2 and all(label for label in labels)
