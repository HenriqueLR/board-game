from app.board.default import BoardDefault


class TestBoardProperts:

    def setup_class(self):
        self.board = BoardDefault()

    def teardown_class(self):
        del self.board

    def test_owners_init(self):
        assert len(self.board.owners) == 20

    def test_sale_value_init(self):
        assert len(self.board.sale_value) == 20

    def test_rent_init(self):
        assert len(self.board.rent) == 20
