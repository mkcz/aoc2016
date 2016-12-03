#!/usr/bin/python3


class SantaAgent:
    headings = {"N": 0, "E": 90, "S": 180, "W": 270}  # type: dict[str, int]
    int_headings = {0: "N", 90: "E", 180: "S", 270: "W"}  # type: dict[int, str]
    multipliers = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}  # type: dict[str, (int, int)]
    x = 0  # type: int
    y = 0  # type: int
    heading = "N"  # type: str

    def reset(self):
        self.x = 0  # type: int
        self.y = 0  # type: int
        self.heading = "N"  # type: str

    def move(self, step: str):
        turn = step[:1]
        distance = int(step[1:])
        self.heading = self._new_heading(self.heading, turn)
        self.x += distance * self.multipliers[self.heading][0]
        self.y += distance * self.multipliers[self.heading][1]

    def travel_distance(self):
        return abs(self.x) + abs(self.y)

    def position(self):
        return "H: {} X: {} Y: {}".format(self.heading, self.x, self.y)

    def _new_heading(self, heading: str, turn: str):
        int_turn = 90 if turn == "R" else -90
        int_heading = self.headings[heading] + int_turn
        if int_heading < 0:
            int_heading = 270
        if int_heading > 270:
            int_heading = 0
        return self.int_headings[int_heading]


def should_quit(command):
    return command in ["quit", "q"]


if __name__ == "__main__":
    raw_directions = ""  # type: str
    agent = SantaAgent()
    while not should_quit(raw_directions):
        raw_directions = input("directions: ")  # type: str
        if not should_quit(raw_directions):
            agent.reset()
            print("Position: [{}]".format(agent.position()))
            directions = raw_directions.replace(" ", "").split(",")  # type: list[str]
            for direction in directions:
                agent.move(direction)
                print("Position: [{}]".format(agent.position()))
            print("Distance between LZ and EBH is {}".format(agent.travel_distance()))
    print("It's over, you can go outside and play now")
