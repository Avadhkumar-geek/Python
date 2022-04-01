import random


class Initializer:

    def __init__(self):
        self.arr = None
        self.n = None

    def ran(self):
        self.n = int(input('Enter range: '))

    def gen(self):
        self.arr = []
        for i in range(10):
            self.arr.append(random.randrange(0, self.n))
        print('Randomly generated Array: ', self.arr)


class Performer(Initializer):
    def __init__(self):
        Initializer.__init__(self)
        # Or we can use 'super().__init__()'

    def bubble(self):
        for i in range(len(self.arr)):
            for j in range(len(self.arr) - 1):
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
        print('Sorted Array: ', self.arr)


start = Performer()
start.ran()
start.gen()
start.bubble()
