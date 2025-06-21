import pprint
from collections.abc import Iterator, Callable
import re
from enum import Enum
from typing import TypeVar, Generic


class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)
    UPLEFT = (-1, -1)
    UPRIGHT = (-1, 1)
    DOWNLEFT = (1, -1)
    DOWNRIGHT = (1, 1)


T = TypeVar("T")


class Grid(Generic[T]):
    def __init__(self, rows: list[list[T]]) -> None:
        self.grid: list[list[T]] = rows
        self._x_length: int = len(rows) if rows else 0
        self._y_length: int = len(rows[0]) if rows else 0
        # Infinite grid?

    def __repr__(self) -> str:
        return repr(self.grid)

    def read(self, x: int, y: int) -> T:
        if x >= self._x_length or y >= self._y_length or y < 0 or x < 0:
            raise IndexError(f"Tried to read {x, y} but the boundary is {self._x_length, self._y_length}")
        return self.grid[x][y]

    def read_neighbour(self, direction: Direction, x: int, y: int) -> T:
        return self.grid[x + direction.value[0]][y + direction.value[1]]


def load_to_str_iter(path: str) -> Iterator[str]:
    r"""Loads a file, strips \n and returns an iterator."""
    return (line.strip("\n") for line in open(path))


def load_to_tuple_regex_iter(path: str, regex: str, datatype: Callable):
    for line in open(path):
        if columns := re.findall(regex, line):
            yield tuple(datatype(text) for text in columns)
        else:
            raise ValueError(f"No regex match found for {regex} in {line[:100]}...")


def load_to_tuple_iter(path: str, datatype: Callable) -> Iterator[tuple]:
    """Loads a file and returns space-separated text in a collection."""
    return load_to_tuple_regex_iter(path, r"\S+", datatype)


def load_to_grid(path: str, datatype: Callable) -> Grid:
    grid = [[datatype(y) for y in x if y != "\n"] for x in open(path)]
    return Grid[datatype](grid)


print(load_to_str_iter("./utility/input/any_cols.txt").__next__())
print(load_to_tuple_iter("./utility/input/any_cols.txt", int).__next__())
print(load_to_tuple_regex_iter("./utility/input/text_search.txt", r"mul\(\d+,\d+\)", str).__next__())
a = load_to_grid("./utility/input/grid_unique.txt", str)
print(a)
print(a.read(1, 1))
print(a.read_neighbour(Direction.UPLEFT, 1, 1))
