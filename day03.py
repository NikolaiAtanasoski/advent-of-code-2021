from pathlib import Path
from collections import Counter


def load_input(file_name):
    with open(file_name, "r") as file:
        return file.read().splitlines()


filename = f"{Path(__file__).stem}.input"
numbers = load_input(filename)

oxygen = numbers.copy()  # gamma rate -> most common bit
co2 = numbers.copy()  # epsilon rate -> least common bit

index = 0
while len(oxygen) > 1:
    jojo = [x[index] for x in oxygen]
    _count = Counter(jojo)
    if _count['1'] >= _count['0']:
        oxygen = [x for x in oxygen if x[index] == '1']
    elif _count['1'] < _count['0']:
        oxygen = [x for x in oxygen if x[index] == '0']
    index += 1

print(f"oxygen: {oxygen}")

index = 0
while len(co2) > 1:
    jojo = [x[index] for x in co2]
    _count = Counter(jojo)
    if _count['1'] >= _count['0']:
        co2 = [x for x in co2 if x[index] == '0']
    elif _count['1'] < _count['0']:
        co2 = [x for x in co2 if x[index] == '1']
    index += 1

print(f"co2: {co2}")

result = int(oxygen[0], 2) * int(co2[0], 2)
print(result)
