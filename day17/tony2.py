class Cube(object):
    cubes = {}

    def __new__(cls, x: int, y:int, z:int, w:int, active: bool=False):
        if (x, y, z, w) in cls.cubes:
            return cls.cubes[x, y, z, w]
        else:
            return super(Cube, cls).__new__(cls)

    def __init__(self, x: int, y: int, z: int, w:int, active: bool = False):
        if 'x' not in dir(self):
            self.x = x
            self.y = y
            self.z = z
            self.w = w
            self.active = active
            self.__class__.cubes[x, y, z, w] = self

    def __str__(self):
        return str([self.x, self.y, self.z, self.w, self.active])

    def count_neighbor(self):
        s = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                for k in [-1, 0, 1]:
                    for l in [-1, 0, 1]:
                        if not 0 == i == j == k == l:
                            cube = Cube(i+self.x, j+self.y, k+self.z, l+self.w)
                            s += cube.active
        return s

    @classmethod
    def next_step(cls):
        next_state = []

        keys = list(cls.cubes.keys())
        for x, y, z, w in keys:  # J'ai fait le malin, je suis tombé dans le ravin
            Cube(x, y, z, w).count_neighbor()

        keys = list(cls.cubes.keys())
        for x, y, z, w in keys:
            if cls.cubes[x, y, z, w].active :
                if cls.cubes[x, y, z, w].count_neighbor() not in [2, 3]:
                    next_state.append([x, y, z, w, False])
            elif cls.cubes[x, y, z, w].count_neighbor() == 3:
                next_state.append([x, y, z, w, True])

        for state in next_state:
            cls.cubes[state[0], state[1], state[2], state[3]].active = state[4]

    @classmethod
    def populate_from_file(cls, filename):
        with open(filename, "r") as f:
            lines = f.readlines()
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                Cube(i, j, 0, 0, lines[i][j] == "#")

    @classmethod
    def count_all_active(cls):
        return sum([cls.cubes[c].active for c in cls.cubes])


if __name__ == "__main__":
    Cube.populate_from_file("input.txt")
    # print([[c.x, c.y, c.z] for c in Cube.cubes.values() if c.active])
    for i in range(6):
        Cube.next_step()
    print(Cube.count_all_active())
