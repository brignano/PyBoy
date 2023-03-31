#
# License: See LICENSE.md file
# GitHub: https://github.com/Baekalfen/PyBoy
#

import os
import sys

# Makes us able to import PyBoy from the directory below
file_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, file_path + "/..")

from pyboy import PyBoy, WindowEvent # isort:skip

# Check if the ROM is given through argv
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    print("Usage: python gamewrapper_pokemon.py [ROM file]")
    exit(1)

quiet = "--quiet" in sys.argv
pyboy = PyBoy(filename, window_type="headless" if quiet else "SDL2", window_scale=3, debug=not quiet, game_wrapper=True)
pyboy.set_emulation_speed(0)
assert pyboy.cartridge_title() == "POKEMON RED"

pokemon = pyboy.game_wrapper()
pokemon.start_game() # The timer_div works like a random seed in Tetris

assert pokemon.pokedex == []

# Checking that a reset on the same `timer_div` results in the same Tetromino
pokemon.reset_game(timer_div=0x00)

pyboy.tick()
pyboy.send_input(WindowEvent.PRESS_BUTTON_START)
pyboy.tick()


print("Final game board mask:")
print(pokemon)

pyboy.stop()
