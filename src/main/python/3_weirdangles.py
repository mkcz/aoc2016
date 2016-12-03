#!/usr/bin/python3


class TriangleCounter:
    number_triangles = 0  # type: int

    def reset(self):
        self.number_triangles = 0

    def consume(self, weirdangles: list):
        sides = [[int(side) for side in weirdangle.strip().split()] for weirdangle in weirdangles]
        for i in range(0, 3):
            self._consume(sides[0][i], sides[1][i], sides[2][i])

    def _consume(self, a: int, b: int, c: int):
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
                weirdangles = []  # type: list[str]
                inx = 0
                for triangle_definition in triangle_definitions:
                    if inx != 3:
                        weirdangles.append(triangle_definition.rstrip('\n'))
                        inx += 1
                    if inx == 3:
                        triangle_counter.consume(weirdangles)
                        inx = 0
                        weirdangles.clear()
                print("Number of valid triangles is {}".format(triangle_counter.number_triangles))
    print("It's over, you can go outside and play now")
