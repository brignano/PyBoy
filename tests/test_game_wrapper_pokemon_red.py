#
# License: See LICENSE.md file
# GitHub: https://github.com/Baekalfen/PyBoy
#

import os
import platform
import sys

import numpy as np
from pyboy import PyBoy, WindowEvent

py_version = platform.python_version()[:3]
is_pypy = platform.python_implementation() == "PyPy"


def test_pokemon_red_basics(pokemon_red_rom):
    pyboy = PyBoy(pokemon_red_rom, window_type="dummy", game_wrapper=True)
    pyboy.set_emulation_speed(0)
    assert pyboy.cartridge_title() == "POKEMON RED"

    pokemon_red = pyboy.game_wrapper()
    pokemon_red.start_game()

    pyboy.stop()