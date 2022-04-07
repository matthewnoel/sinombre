from world import World

MAX_ITERATION_COUNT = 10
WORLD_LENGTH = 50


def main():
    world = World(WORLD_LENGTH)
    print(world)
    world.incrementTime()
    print(world)


main()
