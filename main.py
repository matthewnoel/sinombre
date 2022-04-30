import keyboard
import os
import random
import sys
import time

from box import Box
from world import World

MAX_ITERATION_COUNT = 500
SLEEP_SECONDS = 0.1
WORLD_LENGTH = 65
seed = random.randrange(0, sys.maxsize)
world = World(WORLD_LENGTH)
box = Box()
wants_quit = False
is_paused = False


clear = lambda: os.system("cls" if os.name in ("nt", "dos") else "clear")


def onPress(event):
    global wants_quit
    global is_paused
    if event.name == "q":
        wants_quit = True
    elif event.name == "space":
        is_paused = not is_paused
        box.set("Simulating", not is_paused)
    elif event.name == "n" and is_paused:
        world.incrementTime()
        box.set("Time", world.iteration)
        render()


def render():
    clear()
    print(world)
    print(box)


def main():
    keyboard.on_press(onPress)
    box.set("Simulating", True)
    box.set("Seed", seed)
    render()

    while world.iteration < MAX_ITERATION_COUNT:
        if wants_quit:
            box.set("Outcome", "User quit")
            break
        if is_paused:
            continue
        time.sleep(SLEEP_SECONDS)
        is_incrementable = world.incrementTime()
        box.set("Time", world.iteration)
        render()
        if not is_incrementable:
            box.set("Outcome", "Died out")
            break
    if world.iteration == MAX_ITERATION_COUNT - 1:
        box.set("Outcome", "Max interations hit")
    box.set("Simulating", False)
    render()
    return 0


if len(sys.argv) == 3 and sys.argv[1] == "--seed":
    seed_arg = int(sys.argv[2])
    random.seed(seed_arg)
    seed = seed_arg
main()
