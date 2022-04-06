from world import World

MAX_ITERATION_COUNT = 10
WORLD_LENGTH = 50


def main():
    world = World(WORLD_LENGTH)
    for i in world.voxels:
        for j in i:
            for k in j:
                print(k)


main()
