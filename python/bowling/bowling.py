class Game:
    def __init__(self):
        self.rolls = []

    def roll(self, pins: int):
        self.rolls.append(pins)

    def score(self):
        score = 0
        rr = self.rolls
        print(rr)
        f = 0
        while f < len(rr):
            if f == len(rr) - 1:
                score += rr[f]
                f += 1
            elif rr[f] + rr[f + 1] == 10:  ## have spare!
                score += rr[f] + rr[f + 1] + rr[f + 2]
                if f == len(rr) - 3:
                    return score + rr[f + 2]
                f += 2  ## next frame
            elif rr[f] == 10:  ## have strike!
                score += rr[f] + rr[f + 1] + rr[f + 2]
                if f == len(rr) - 3:
                    return score
                f += 1  # When there is a strike the frame ends
            else:  ## no spare or strike
                score += rr[f] + rr[f + 1]
                f += 2  ## next frame
            print(f, score)
        return score
