import pytest
import util as u


class TestGrid:
    grid_unique: u.Grid[str] = u.load_grid("./utility/input/grid_unique.txt", str)
    grid_rectangle: u.Grid[str] = u.load_grid("./utility/input/grid_rectangle.txt", str)
    grid_small: u.Grid[str] = u.load_grid("./utility/input/grid_small.txt", str)
    grid_smallest: u.Grid[str] = u.load_grid("./utility/input/grid_smallest.txt", str)

    def test_init(self):
        assert self.grid_rectangle._col_length == 12
        assert self.grid_rectangle._row_length == 2

    def test_read(self):
        assert self.grid_unique.read(0, 0) == "A"
        assert self.grid_unique.read(1, 2) == "F"
        assert self.grid_unique.read(2, 0, True) == "G"
        assert self.grid_unique.read(2, 5, False) == None

        assert self.grid_rectangle.read(1, 5) == "B"
        assert self.grid_rectangle.read(3, 3, False) == None

        with pytest.raises(IndexError):
            self.grid_unique.read(-1, 0)
            self.grid_unique.read(3, 3)
            self.grid_unique.read(3, 3, True)

    def test_read_neighbour(self):
        assert self.grid_unique.read_neighbour(u.Direction.DOWN, 0, 0) == "D"
        assert self.grid_unique.read_neighbour(u.Direction.UPLEFT, 2, 2) == "E"
        assert self.grid_unique.read_neighbour(u.Direction.DOWNRIGHT, 0, 0) == "E"
        assert self.grid_unique.read_neighbour(u.Direction.RIGHT, 2, 0) == "H"
        assert self.grid_unique.read_neighbour(u.Direction.LEFT, 0, 1) == "A"
        assert self.grid_unique.read_neighbour(u.Direction.DOWNLEFT, 1, 2) == "H"
        assert self.grid_unique.read_neighbour(u.Direction.DOWNLEFT, 1, -5, False) == None

        with pytest.raises(IndexError):
            self.grid_unique.read_neighbour(u.Direction.RIGHT, 2, 2)
            self.grid_unique.read_neighbour(u.Direction.LEFT, 0, 0)
            self.grid_unique.read_neighbour(u.Direction.UPLEFT, 0, 0)

    def test_sequences(self):
        with pytest.raises(ValueError):
            list(self.grid_small.find_sequences(""))
            list(self.grid_smallest.find_sequences("S"))

        assert len(list(self.grid_small.find_sequences("XMMM"))) == 3
        assert len(list(self.grid_smallest.find_sequences("MAS"))) == 4
        assert len(list(self.grid_smallest.find_sequences("SM"))) == 8
