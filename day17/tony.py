class Cube(object):
    cubes = {}

    def __new__(cls, x: int, y:int , z:int , active: bool=False):
        if (x, y, z) in cls.cubes:
            return cls.cubes[x, y, z]
        else:
            return super(Cube, cls).__new__(cls)

    def __init__(self, x: int, y: int, z: int, active: bool = False):
        if 'x' not in dir(self):
            self.x = x
            self.y = y
            self.z = z
            self.active = active
            self.__class__.cubes[x, y, z] = self

    def __str__(self):
        return str([self.x, self.y, self.z, self.active])

    def count_neighbor(self):
        s = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                for k in [-1, 0, 1]:
                    if not 0 == i == j == k:
                        cube = Cube(i+self.x, j+self.y, k+self.z)
                        s += cube.active
        return s

    @classmethod
    def next_step(cls):
        next_state = []

        keys = list(cls.cubes.keys())
        for x, y, z in keys:  # J'ai fait le malin, je suis tombé dans le ravin
            Cube(x, y, z).count_neighbor()

        keys = list(cls.cubes.keys())
        for x, y, z in keys:
            if cls.cubes[x, y, z].active :
                if cls.cubes[x, y, z].count_neighbor() not in [2, 3]:
                    next_state.append([x, y, z, False])
            elif cls.cubes[x, y, z].count_neighbor() == 3:
                next_state.append([x, y, z, True])

        for state in next_state:
            cls.cubes[state[0], state[1], state[2]].active = state[3]

    @classmethod
    def populate_from_file(cls, filename):
        with open(filename, "r") as f:
            lines = f.readlines()
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                Cube(i, j, 0, lines[i][j] == "#")

    @classmethod
    def count_all_active(cls):
        return sum([cls.cubes[c].active for c in cls.cubes])


if __name__ == "__main__":
    Cube.populate_from_file("input.txt")
    # print([[c.x, c.y, c.z] for c in Cube.cubes.values() if c.active])
    for i in range(6):
        Cube.next_step()
    print(Cube.count_all_active())
