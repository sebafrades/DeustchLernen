import random

class Trainer:

    def __init__(self, words):
        self.words = words
        self.index = 0

    def random_word(self):

        weights = []

        for word in self.words:

            weight = (word.wrong + 1) / (word.correct + 1)

            weights.append(weight)

        return random.choices(
            self.words,
            weights=weights,
            k=1
        )[0]

    def next_word(self):

        word = self.words[self.index]

        self.index += 1

        if self.index >= len(self.words):
            return None

        return word