import re
from collections.abc import Callable, Iterator
from enum import Enum
from typing import Generic, Optional, TypeVar


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
    """Represents a grid which can be accessed with coordinates."""

    def __init__(self, rows: list[list[T]]) -> None:
        self._grid: list[list[T]] = rows
        self._col_length: int = len(rows[0]) if rows else 0
        self._row_length: int = len(rows)

    def __repr__(self) -> str:
        return repr(self._grid)

    def read(self, row: int, col: int, strict: bool = True) -> Optional[T]:
        if col >= self._col_length or row >= self._row_length or row < 0 or col < 0:
            if not strict:
                return None
            else:
                raise IndexError(f"Tried to read {row, col} but the boundary is {self._row_length, self._col_length}")
        return self._grid[row][col]

    def read_neighbour(self, direction: Direction, row: int, col: int, strict: bool = True) -> Optional[T]:
        """Reads a value from the matrix in the direction supplied."""
        return self.read(row + direction.value[0], col + direction.value[1], strict)

    def find_sequences(self, sequence: str) -> Iterator[tuple[int, int, Direction]]:
        """Finds character sequences in the grid, in any direction. Returns coordinates and sequence direction."""
        sequence_length: int = len(sequence)
        if sequence_length < 2:
            raise ValueError(
                f"Sequence must at least be 2, but is {sequence_length} characters long; (seq={sequence}).")

        for row in range(self._row_length):
            for col in range(self._col_length):
                for d in Direction:  # TODO: We might be able to skip some directions, when close to the edges...
                    for step_counter in range(sequence_length):
                        if self.read(row + d.value[0] * step_counter, col + d.value[1] * step_counter, False) != sequence[step_counter]:
                            break
                    else:
                        # for-else: Only runs if the for loop did not terminate with break
                        # => In this case: There were no wrong chars in the found sequence
                        yield row, col, d

# Input parser


def load_str(path: str) -> Iterator[str]:
    r"""Loads an input file, strips \n and returns an iterator."""
    with open(path) as input_file:
        yield from (line.strip("\n") for line in input_file)


def load_split(path: str, split_char: str, datatype: Callable = str) -> Iterator:
    """Loads an input file and splits at the provided character."""
    yield from (tuple(datatype(item) for item in x.split(split_char)) for x in load_str(path))


def load_regex_text_search(path: str, regex: str, datatype: Callable = str) -> Iterator:
    """Loads an input file and looks for the supplied regex, yields from iterator over all matches found."""
    with open(path) as input_file:
        for line in input_file:
            if columns := re.findall(regex, line):
                yield from (datatype(text) for text in columns)
            else:
                raise ValueError(f"No regex match found for {regex} in {line[:100]}...")


def load_grid(path: str, datatype: Callable = str) -> Grid:
    """Loads an input file into memory and returns a Grid implementation."""
    with open(path) as input_file:
        grid = [[datatype(val) for val in row if val != "\n"] for row in input_file]
        return Grid[datatype](grid)

# def load_space_separated(path: str, datatype: Callable = str) -> Iterator[tuple]:
#     """Loads an input file and returns space-separated text in a tuple."""
#     return load_regex_text_search(path, r"\S+", datatype)


print(load_regex_text_search("./utility/input/text_search.txt", r"mul\(\d+,\d+\)", str).__next__())
load_split("./utility/input/two_cols_split.txt", "|", int)
