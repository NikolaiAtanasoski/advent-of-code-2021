from pathlib import Path


class AmkBit:

    def __init__(self):
        self.ones = 0
        self.zeroes = 0

    def add_count(self, bit: str):
        if bit == "1":
            self.ones += 1
        elif bit == "0":
            self.zeroes += 1

    def get_most_least_common(self):
        if self.ones > self.zeroes:
            return (1, 0)
        return (0, 1)


def load_input(file_name):
    with open(file_name, "r") as file:
        return file.read().splitlines()


filename = f"{Path(__file__).stem}.input"
numbers = load_input(filename)

gamma = 0  # gamma rate -> most common bit
epsilon = 0  # epsilon rate -> least common bit

amk_bits = []
for i in range(0, 12):
    amk_bits.append(AmkBit())


for number in numbers:
    for i in range(0, 12):
        amk_bits[i].add_count(number[i])

mulitplier = 2 ** 11
for amk_bit in amk_bits:
    _gamma, _epsilon = amk_bit.get_most_least_common()
    gamma += _gamma * mulitplier
    epsilon += _epsilon * mulitplier
    mulitplier = int(mulitplier / 2)

result = gamma * epsilon
print(f"gamma: {gamma}, epsilon: {epsilon}")
print(f"result: {result}")
