import util


class TestLoads:
    any_cols = list(util.load_str("./utility/input/any_cols.txt"))
    # space_separated = list(util.load_space_separated("./utility/input/any_cols.txt", int))

    def test_load_str(self):
        assert len(self.any_cols) == 1000
        assert type(self.any_cols[4]) == str

    # def test_load_space_separated(self):
    #     assert len(self.space_separated) == 1000
    #     assert type(self.any_cols[711]) == tuple
