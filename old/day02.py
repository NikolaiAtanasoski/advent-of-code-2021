from pathlib import Path


def load_input(file_name):
    with open(file_name, "r") as file:
        return file.read().splitlines()


filename = f"{Path(__file__).stem}.input"
print(filename)
instructions = load_input(filename)
print(instructions)

aim = 0
horizontal = 0
depth = 0

for command in instructions:
    print(command)
    name = command.split(" ")[0]
    value = command.split(" ")[1]

    if name == "down":
        aim += int(value)
    elif name == "up":
        aim -= int(value)
    elif name == "forward":
        horizontal += int(value)
        depth += (aim * int(value))
    else:
        print(f"unknown command found: {command}")

result = horizontal * depth
print(f"result : {result}")