#!/usr/bin/python3


class TriangleCounter:
    number_triangles = 0  # type: int

    def reset(self):
        self.number_triangles = 0

    def consume(self, definition: str):
        (a, b, c) = [int(side) for side in definition.strip().split()]
        if (a + b) <= c or (a + c) <= b or (b + c) <= a:
            return
        self.number_triangles += 1


def should_quit(command):
    return command in ["quit", "q"]


if __name__ == "__main__":
    input_file = ""  # type: str
    triangle_counter = TriangleCounter()
    while not should_quit(input_file):
        input_file = input("input_file: ")  # type: str
        triangle_counter.reset()
        if not should_quit(input_file):
            with open(input_file) as file:
                triangle_definitions = file.readlines()
                for triangle_definition in triangle_definitions:
                    triangle_counter.consume(triangle_definition.rstrip('\n'))
                print("Number of valid triangles is {}".format(triangle_counter.number_triangles))
    print("It's over, you can go outside and play now")
