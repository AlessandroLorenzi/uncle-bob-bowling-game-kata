class ScoreCalculatorService:
    __LAST_STRIKE_FRAME_SIZE = 3
    __REGULAR_FRAME_SIZE = 2
    __SPARE_FRAME_SIZE = 2
    __STRIKE_FRAME_SIZE = 1
    __LAST_THROW_SIZE = 1
    __MAX_PINS_PER_FRAME = 10

    def __init__(self, rolls: list[int]):
        self.rolls = rolls
        self.score = 0

    def calculate(self):
        while 0 < len(self.rolls):
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
            self.__execute_regular_frame()

    def __frame_is_spare(self) -> bool:
        return (self.rolls[0] + self.rolls[1]) == self.__MAX_PINS_PER_FRAME

    def __frame_is_strike(self) -> bool:
        return self.rolls[0] == self.__MAX_PINS_PER_FRAME

    def __is_last_throw(self) -> bool:
        return len(self.rolls) == 1

    def __execute_spare(self):
        self.__sum_next_throws_to_score(3)
        self.__drop_frame(self.__SPARE_FRAME_SIZE)

    def __execute_strike(self):
        self.__sum_next_throws_to_score(3)
        if 0 == len(self.rolls) - self.__LAST_STRIKE_FRAME_SIZE:
            self.__terminate_rolls()
            return
        self.__drop_frame(self.__STRIKE_FRAME_SIZE)

    def __execute_last_throw(self):
        self.__sum_next_throws_to_score(1)
        self.__drop_frame(self.__LAST_THROW_SIZE)

    def __execute_regular_frame(self):
        self.__sum_next_throws_to_score(2)
        self.__drop_frame(self.__REGULAR_FRAME_SIZE)

    def __drop_frame(self, spaces: int):
        self.rolls = self.rolls[spaces:]

    def __terminate_rolls(self):
        self.rolls = []

    def __sum_next_throws_to_score(self, throws: int):
        for t in range(0, throws):
            self.score += self.rolls[t]
