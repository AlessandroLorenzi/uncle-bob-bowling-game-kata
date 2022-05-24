from .ScoreCalculatorService import ScoreCalculatorService


class Game:
    def __init__(self):
        self.rolls = []

    def roll(self, pins: int):
        self.rolls.append(pins)

    def calculate_score(self):
        score_calculator_service = ScoreCalculatorService(self.rolls)
        return score_calculator_service.calculate()
