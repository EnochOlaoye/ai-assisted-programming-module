"""A compact email address validator."""

from __future__ import annotations

import re


_EMAIL = re.compile(
    r"^[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+"
    r"@[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?"
    r"(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?)+$"
)


def is_valid_email(address: str) -> bool:
    """Return whether *address* matches a conventional email shape."""
    return (
        isinstance(address, str)
        and len(address) <= 254
        and bool(_EMAIL.fullmatch(address))
    )
