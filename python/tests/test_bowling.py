from bowling import Game


class TestBowling:
    def test_unluckly_game(self):
        self.g = Game()
        self.roll_many(20, 0)
        assert 0 == self.g.calculate_score()

    def test_all_one(self):
        self.g = Game()
        self.roll_many(20, 1)
        assert 20 == self.g.calculate_score()

    def test_spare(self):
        self.g = Game()
        self.g.roll(5)
        self.g.roll(5)
        self.g.roll(3)
        self.roll_many(17, 0)

        assert 16 == self.g.calculate_score()

    def test_strike(self):
        self.g = Game()
        # First Frame
        self.g.roll(10)
        # Second Frame
        self.g.roll(2)
        self.g.roll(3)
        # 3rd to 10th all zeroes
        self.roll_many(8 * 2, 0)

        assert 20 == self.g.calculate_score()

    def test_last_strike(self):
        self.g = Game()
        self.roll_many(9 * 2, 0)
        self.g.roll(10)
        self.g.roll(2)
        self.g.roll(3)

        assert 15 == self.g.calculate_score()

    def test_last_spare(self):
        self.g = Game()
        self.roll_many(9 * 2, 0)
        self.g.roll(5)
        self.g.roll(5)
        self.g.roll(3)

        assert 16 == self.g.calculate_score()

    def test_rookieroad_example(self):
        # Source: https://www.rookieroad.com/bowling/scoring-rules/
        self.g = Game()
        # Frame 1
        self.g.roll(5)
        self.g.roll(4)
        # Frame 2
        self.g.roll(4)
        self.g.roll(6)  # Spare!
        # Frame 3
        self.g.roll(7)
        self.g.roll(0)
        # Frame 4
        self.g.roll(10)  # Strike!
        # Frame 5
        self.g.roll(10)  # Strike!
        # Frame 6
        self.g.roll(10)  # Strike!
        # Frame 7
        self.g.roll(5)
        self.g.roll(3)
        # Frame 8
        self.g.roll(6)
        self.g.roll(4)  # Spare!
        # Frame 9
        self.g.roll(4)
        self.g.roll(6)  # Spare!

        # Frame 10
        self.g.roll(10)  # Strike!
        self.g.roll(10)  # Strike!
        self.g.roll(10)  # Strike!

        assert 178 == self.g.calculate_score()

    def test_perfect_score(self):
        self.g = Game()
        self.roll_many(12, 10)
        assert 300 == self.g.calculate_score()

    def roll_many(self, n, pins):
        for i in range(n):
            self.g.roll(pins)
