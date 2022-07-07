from app.player.npc import NpcImpulsive, NpcDemanding, NpcCautious, NpcRandom


class TestBoardProperts:

    def setup_class(self):
        self.impulsive = NpcImpulsive()
        self.demanding = NpcDemanding()
        self.cautious = NpcCautious()
        self.random = NpcRandom()

    def teardown_class(self):
        del self.impulsive
        del self.demanding
        del self.cautious
        del self.random

    def test_init_credit_players(self):
        assert self.impulsive._credit == 300
        assert self.demanding._credit == 300
        assert self.cautious._credit == 300
        assert self.random._credit == 300

    def test_init_position_players(self):
        assert self.impulsive._position == 0
        assert self.demanding._position == 0
        assert self.cautious._position == 0
        assert self.random._position == 0

    def test_init_disabled_players(self):
        assert self.impulsive.disabled is False
        assert self.demanding.disabled is False
        assert self.cautious.disabled is False
        assert self.random.disabled is False
