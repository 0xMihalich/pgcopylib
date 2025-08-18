from struct import unpack

from .nullables import if_nullable


@if_nullable
def to_text(binary_data: bytes) -> str:
    """Unpack text value."""

    return binary_data.decode("utf-8", errors="replace")


@if_nullable
def to_macaddr(binary_data: bytes) -> str:
    """Unpack macaddr и macaddr8 value."""

    return ":".join(
        f"{byte:02x}"
        for byte in unpack(
            f">{len(binary_data)}B",
            binary_data,
        )
    ).upper()


@if_nullable
def to_bytea(binary_data: bytes) -> bytes:
    """Unpack bytea value."""

    return binary_data
