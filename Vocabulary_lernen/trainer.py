import random


class Trainer:

    def __init__(self, words):
        self.words = words
        self.index = 0
        self.missed_words = []

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

        if self.index >= len(self.words):
            return None

        word = self.words[self.index]
        self.index += 1

        return word

    def mark_missed(self, word):
        if word not in self.missed_words:
            self.missed_words.append(word)

    def has_missed_words(self):
        return len(self.missed_words) > 0

    def retry_missed(self):
        """Restart a consecutive round using only the missed words."""
        self.words = self.missed_words
        self.index = 0
        self.missed_words = []