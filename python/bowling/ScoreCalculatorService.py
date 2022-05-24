class ScoreCalculatorService:
    __LAST_STRIKE_FRAME_SIZE = 3
    __REGULAR_FRAME_SIZE = 2
    __SPARE_FRAME_SIZE = 2
    __STRIKE_FRAME_SIZE = 1
    __LAST_THROW_SIZE = 1

    def __init__(self, rolls: list[int]):
        self.rolls = rolls
        self.rolls_cursor = 0
        self.score = 0

    def calculate(self):
        while self.rolls_cursor < len(self.rolls):
            self.__calculate_next_frame()

        return self.score

    def __calculate_next_frame(self):
        if self.__is_last_throw():
            self.__execute_last_throw()

        elif self.__frame_is_spare():
            self.__execute_spare()

        elif self.__frame_is_strike():
            self.__execute_strike()

        else:
            self.__execute_regular_throw()

        
    def __frame_is_spare(self) -> bool:
        return (self.rolls[self.rolls_cursor] + self.rolls[self.rolls_cursor + 1]) == 10

    def __frame_is_strike(self) -> bool:
        return self.rolls[self.rolls_cursor] == 10

    def __is_last_throw(self) -> bool:
        return self.rolls_cursor == len(self.rolls) - 1

    def __execute_spare(self):
        self.score += (
            self.rolls[self.rolls_cursor]
            + self.rolls[self.rolls_cursor + 1]
            + self.rolls[self.rolls_cursor + 2]
        )
        self.__advance_rolls_curor(self.__SPARE_FRAME_SIZE)

    def __execute_strike(self):
        self.score += (
            self.rolls[self.rolls_cursor]
            + self.rolls[self.rolls_cursor + 1]
            + self.rolls[self.rolls_cursor + 2]
        )
        if self.rolls_cursor == len(self.rolls) - self.__LAST_STRIKE_FRAME_SIZE:
            self.__advance_rolls_curor(self.__LAST_STRIKE_FRAME_SIZE)
            return
        self.__advance_rolls_curor(self.__STRIKE_FRAME_SIZE)

    def __execute_last_throw(self):
        self.score += self.rolls[self.rolls_cursor]
        self.__advance_rolls_curor(self.__LAST_THROW_SIZE)

    def __execute_regular_throw(self):
        self.score += self.rolls[self.rolls_cursor] + self.rolls[self.rolls_cursor + 1]
        self.__advance_rolls_curor(self.__REGULAR_FRAME_SIZE)

    def __advance_rolls_curor(self, spaces: int):
        self.rolls_cursor += spaces

