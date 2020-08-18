letter_pairs = (''.join(p) for p in product(letters, letters))
numbers = (str(i).zfill(3) for i in range(1000))
names = [l + n for l, n in product(letter_pairs, numbers)]
shuffle(names)
NAMES = iter(names)


class Robot(object):
    def __init__(self):
        self.reset()

    def reset(self):
        self.name = next(NAMES)
