import os
import random
import sys
import time

from box import Box
from world import World

MAX_ITERATION_COUNT = 500
SLEEP_SECONDS = 0.1
WORLD_LENGTH = 75
seed = random.randrange(0, sys.maxsize)


clear = lambda: os.system("cls" if os.name in ("nt", "dos") else "clear")


def main():
    world = World(WORLD_LENGTH)
    box = Box()
    box.set("Seed", seed)
    clear()
    print(world)
    print(box)
    i = 0
    while i < MAX_ITERATION_COUNT:
        time.sleep(SLEEP_SECONDS)
        is_incrementable = world.incrementTime()
        box.set("Time", i)
        clear()
        print(world)
        print(box)
        if not is_incrementable:
            break
        i += 1
    return 0


if len(sys.argv) == 3 and sys.argv[1] == "--seed":
    seed_arg = int(sys.argv[2])
    random.seed(seed_arg)
    seed = seed_arg
main()
