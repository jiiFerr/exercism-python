STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.masked_word = ['_'] * len(word)
        self.word = list(word)

    def guess(self, char):
        if self.status == STATUS_LOSE:
            raise ValueError('Game over man! Game over!')

        if self.status == STATUS_WIN:
            raise ValueError('You have won already!')

        correct_guess = False
        for i in range(len(self.word)):
            if self.masked_word[i] == '_':
                if char.lower() == self.word[i].lower():
                    self.masked_word[i] = char
                    correct_guess = True

        if self.get_masked_word().count('_') < 1:
            self.status = STATUS_WIN
        else:
            if not correct_guess:
                if self.remaining_guesses >= 1:
                    self.remaining_guesses -= 1
                else:
                    self.status = STATUS_LOSE

    def get_masked_word(self):
        return ''.join(self.masked_word)

    def get_status(self):
        return self.status

