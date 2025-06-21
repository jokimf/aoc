import pytest
import util as u


class Tests:
    grid_unique: u.Grid[str] = u.load_to_grid("./utility/input/grid_unique.txt", str)

    def test_read(self):
        assert self.grid_unique.read(0, 0) == "A"
        assert self.grid_unique.read(1, 2) == "F"
        with pytest.raises(IndexError):
            self.grid_unique.read(-1, 0)
            self.grid_unique.read(3, 3)

    def test_read_neighbour(self):
        assert self.grid_unique.read_neighbour(u.Direction.DOWN, 0, 0) == "D"
        assert self.grid_unique.read_neighbour(u.Direction.UPLEFT, 2, 2) == "E"
        assert self.grid_unique.read_neighbour(u.Direction.DOWNRIGHT, 0, 0) == "E"
        assert self.grid_unique.read_neighbour(u.Direction.RIGHT, 2, 0) == "H"
        assert self.grid_unique.read_neighbour(u.Direction.LEFT, 0, 1) == "A"
        assert self.grid_unique.read_neighbour(u.Direction.DOWNLEFT, 1, 2) == "H"

        with pytest.raises(IndexError):
            self.grid_unique.read_neighbour(u.Direction.RIGHT, 2, 2)
            self.grid_unique.read_neighbour(u.Direction.LEFT, 0, 0)
            self.grid_unique.read_neighbour(u.Direction.UPLEFT, 0, 0)
