from decimal import Decimal
from struct import (
    unpack,
    unpack_from,
)
from typing import Union

from .nullables import if_nullable


@if_nullable
def to_bool(binary_data: bytes) -> bool:
    """Unpack bool value."""

    return unpack("!?", binary_data)[0]


@if_nullable
def to_oid(binary_data: bytes) -> int:
    """Unpack oid value."""

    return unpack("!I", binary_data)[0]


@if_nullable
def to_serial2(binary_data: bytes) -> int:
    """Unpack serial2 value."""

    return unpack("!H", binary_data)[0]


@if_nullable
def to_serial4(binary_data: bytes) -> int:
    """Unpack serial4 value."""

    return unpack("!L", binary_data)[0]


@if_nullable
def to_serial8(binary_data: bytes) -> int:
    """Unpack serial8 value."""

    return unpack("!Q", binary_data)[0]


@if_nullable
def to_int2(binary_data: bytes) -> int:
    """Unpack int2 value."""

    return unpack("!h", binary_data)[0]


@if_nullable
def to_int4(binary_data: bytes) -> int:
    """Unpack int4 value."""

    return unpack("!l", binary_data)[0]


@if_nullable
def to_int8(binary_data: bytes) -> int:
    """Unpack int8 value."""

    return unpack("!q", binary_data)[0]


@if_nullable
def to_money(binary_data: bytes) -> float:
    """Unpack money value."""

    return to_int8(binary_data) * 0.01


@if_nullable
def to_float4(binary_data: bytes) -> float:
    """Unpack float4 value."""

    return unpack("!f", binary_data)[0]


@if_nullable
def to_float8(binary_data: bytes) -> float:
    """Unpack float8 value."""

    return unpack("!d", binary_data)[0]


@if_nullable
def to_numeric(binary_data: bytes) -> Decimal:
    """Unpack numeric value."""

    ndigits, weight, sign, dscale = unpack_from(
        "!hhhh",
        binary_data,
    )

    if sign == 0xc000:
        return Decimal("nan")

    is_negative: bool = sign == 0x4000
    digits: list[int] = [
        unpack_from("!h", binary_data[i:i + 2])[-1]
        for i in range(8, 8 + ndigits * 2, 2)
    ]

    numeric = Decimal(0)
    scale = Decimal(10) ** -dscale

    for pos, digit in enumerate(digits):
        power = Decimal(4) * (Decimal(weight) - Decimal(pos))
        term = Decimal(digit) * (Decimal(10) ** power)
        numeric += term

    if is_negative:
        numeric *= -1

    return numeric.quantize(scale)


@if_nullable
def to_point(binary_data: bytes) -> tuple[float, float]:
    """Unpack point value."""

    return unpack("!2d", binary_data)


@if_nullable
def to_line(binary_data: bytes) -> tuple[float, float, float]:
    """Unpack line value."""

    return unpack("!3d", binary_data)


@if_nullable
def to_circle(binary_data: bytes) -> tuple[tuple[float, float], float]:
    """Unpack circle value."""

    *x_y, r = unpack("!3d", binary_data)

    return x_y, r


@if_nullable
def to_lseg(binary_data: bytes) -> list[tuple[float, float]]:
    """Unpack lseg value."""

    x1, y1, x2, y2 = unpack("!4d", binary_data)

    return [(x1, y1), (x2, y2)]


@if_nullable
def to_box(binary_data: bytes) -> tuple[
    tuple[float, float],
    tuple[float, float],
]:
    """Unpack box value."""

    x1, y1, x2, y2 = unpack("!4d", binary_data)

    return (x1, y1), (x2, y2)


@if_nullable
def to_path(binary_data: bytes) -> Union[
    list[tuple[float, float]],
    tuple[tuple[float, float]],
]:
    """Unpack path value."""

    is_closed, length, *path_data = unpack(
        f"!?l{(len(binary_data) - 5) // 8}d",
        binary_data,
    )
    path_data = tuple(
        path_data[i:i + 2]
        for i in range(0, len(path_data), 2)
    )

    return {
        True: tuple,
        False: list,
    }[is_closed](
        path_data[i:i + length]
        for i in range(0, len(path_data), length)
    )


@if_nullable
def to_polygon(binary_data: bytes) -> tuple[tuple[float, float]]:
    """Unpack polygon value."""

    length, *path_data = unpack(
        f"!l{(len(binary_data) - 4) // 8}d",
        binary_data,
    )
    path_data = tuple(
        path_data[i:i + 2]
        for i in range(0, len(path_data), 2)
    )

    return tuple(
        path_data[i:i + length]
        for i in range(0, len(path_data), length)
    )
