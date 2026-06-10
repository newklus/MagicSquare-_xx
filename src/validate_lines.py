"""MagicSquare_XX — validate_lines API (세션 3 Harness)."""

from typing import Literal, TypedDict

MAGIC_CONSTANT = 34

LINE_NAMES: tuple[str, ...] = (
    "R1",
    "R2",
    "R3",
    "R4",
    "C1",
    "C2",
    "C3",
    "C4",
    "D1",
    "D2",
)

Status = Literal["pass", "fail", "incomplete"]


class ValidateResult(TypedDict):
    status: Status
    failed_lines: list[str]


def validate_lines(grid: list[list[int]]) -> ValidateResult:
    ...
