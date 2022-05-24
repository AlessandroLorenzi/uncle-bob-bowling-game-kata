class Game:
    __REGULAR_FRAME_SIZE = 2
    __SPARE_FRAME_SIZE = 2
    __STRIKE_FRAME_SIZE = 1
    __LAST_STRIKE_FRAME_SIZE = 3

    def __init__(self):
        self.rolls = []

    def roll(self, pins: int):
        self.rolls.append(pins)

    def calculate_score(self):
        score = 0
        rolls = self.rolls
        throw = 0

        while throw < len(rolls):
            if self.__is_last_throw(throw):
                score += self.__calculate_last_throw(throw)
                return score

            elif self.__is_spare(throw):
                score += self.__calculate_spare_or_strike(throw)
                throw += self.__SPARE_FRAME_SIZE

            elif self.__is_strike(throw):
                score += self.__calculate_spare_or_strike(throw)
                if throw == len(rolls) - self.__LAST_STRIKE_FRAME_SIZE:
                    return score
                throw += self.__STRIKE_FRAME_SIZE

            else:  ## regular throw
                score += rolls[throw] + rolls[throw + 1]
                throw += self.__REGULAR_FRAME_SIZE  ## next frame

        return score

    def __is_spare(self, throw: int) -> bool:
        return (self.rolls[throw] + self.rolls[throw + 1]) == 10

    def __is_strike(self, throw: int) -> bool:
        return self.rolls[throw] == 10

    def __is_last_throw(self, throw: int) -> bool:
        return throw == len(self.rolls) - 1

    def __calculate_spare_or_strike(self, throw: int) -> int:
        return self.rolls[throw] + self.rolls[throw + 1] + self.rolls[throw + 2]

    def __calculate_last_throw(self, throw: int) -> int:
        return self.rolls[throw]
