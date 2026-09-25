"""A simple email address validator."""

from __future__ import annotations

import re


_EMAIL = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def is_valid_email(address: str) -> bool:
    """Return whether *address* has a basic email-like shape."""
    return (
        isinstance(address, str)
        and len(address) <= 254
        and bool(_EMAIL.fullmatch(address))
    )
