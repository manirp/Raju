class Game():

    def __init__(self):
        self._rolls = []

    def roll(self, pins):
        self._rolls.append(pins)

    def score(self):
        score = 0
        frame_index = 0
        for frame in xrange(10):
            if self._isStrike(frame_index):
                score += 30 + self._strikeBonus(frame_index)
                frame_index += 1
            elif self._isSpare(frame_index):
                score += 9 + self._spareBonus(frame_index)
                frame_index += 2
            else:
                score += 15 + self._missesBonus(frame_index)
                frame_index += 3
        return score

    def _isStrike(self, frame_index):
        return self._rolls[frame_index] == 10

    def _isSpare(self, frame_index):
        return self._rolls[frame_index] + self._rolls[frame_index+1] == 10

    def _strikeBonus(self, frame_index):
        return self._rolls[frame_index+1] + self._rolls[frame_index+2]

    def _spareBonus(self, frame_index):
        return self._rolls[frame_index+2]
		
    def _missesBonus(self, frame_index):
        return self._rolls[frame_index] + self._rolls[frame_index+1]