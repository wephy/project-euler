# Reciprocal cycles

class Dividing:
    def __init__(self, num):
        self.num = num
        self.d = 1
        self.r_list = []
        self.cycle_length = 0
        self.cycle = self.get_cycle()

    def next_digit(self):
        r = self.d % self.num
        if r in self.r_list:
            self.cycle_length = len(self.r_list) - self.r_list.index(r)
            return
        self.r_list.append(r)
        self.d = r*10
        self.next_digit()

    def get_cycle(self):
        self.next_digit()
        return self.cycle_length


longest = {'number': 0, 'length': 0}
for n in range(2, 1000):
    length = Dividing(n).cycle
    if length > longest['length']:
        longest['length'] = length
        longest['number'] = n

print(longest['number'])
