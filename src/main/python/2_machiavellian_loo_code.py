#!/usr/bin/python3


class KeyPadWalker:
    keypad = [[' ', ' ', '1', ' ', ' '],
              [' ', '2', '3', '4', ' '],
              ['5', '6', '7', '8', '9'],
              [' ', 'A', 'B', 'C', ' '],
              [' ', ' ', 'D', ' ', ' ']]  # type: list[list[str]]
    directions = {"U": (-1, 0), "L": (0, -1), "D": (1, 0), "R": (0, 1)}  # type: dict[str, (int, int)]
    x = 2  # type: int
    y = 0  # type: int
    access_code = []  # type: list[str]

    def reset(self):
        self.access_code = []
        self.x = 2
        self.y = 0

    def walk(self, instructions: list):
        for step in instructions:
            x = self.x + self.directions[step][0]
            y = self.y + self.directions[step][1]
            if 0 <= x <= 4 and 0 <= y <= 4 and self.keypad[x][y] is not ' ':
                self.x = x
                self.y = y
        self.access_code.append(self.keypad[self.x][self.y])

    def code(self):
        return "".join(self.access_code)


def should_quit(command):
    return command in ["quit", "q"]


if __name__ == "__main__":
    input_file = ""  # type: str
    key_pad_walker = KeyPadWalker()
    while not should_quit(input_file):
        input_file = input("input_file: ")  # type: str
        key_pad_walker.reset()
        if not should_quit(input_file):
            with open(input_file) as file:
                code_instructions = file.readlines()
                for instructions in code_instructions:
                    key_pad_walker.walk(list(instructions.rstrip('\n')))
                print("Loo access code is {}".format(key_pad_walker.code()))
    print("It's over, you can go outside and play now")
