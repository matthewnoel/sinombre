import os
import time

from world import World

MAX_ITERATION_COUNT = 500
SLEEP_SECONDS = 0.1
WORLD_LENGTH = 50


clear = lambda: os.system("cls" if os.name in ("nt", "dos") else "clear")


def main():
    world = World(WORLD_LENGTH)
    clear()
    print(world)

    i = 0
    while i < MAX_ITERATION_COUNT:
        time.sleep(SLEEP_SECONDS)
        is_incrementable = world.incrementTime()
        clear()
        print(world)
        if not is_incrementable:
            break
        i += 1
    return 0


main()
