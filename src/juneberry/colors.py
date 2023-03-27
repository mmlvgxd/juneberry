# -*- coding: utf-8 -*-
# MIT License
#
# Copyright (c) 2023 mmlvgx
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
'''Juneberry colors'''
from dataclasses import dataclass

from typing import NewType
from typing import Union
from typing import Tuple


__all__ = ('Mode', 'Colour', 'Color')

# Type
R = NewType('R', int)
G = NewType('G', int)
B = NewType('B', int)

# ANSI
ansi256 = '\x1b[{mode};2;{r};{g};{b}m'

RESET = '\033[0m'


# Color mode
class Mode:
    '''Represents a Juneberry color mode'''

    @dataclass
    class Fore:
        '''Foreground'''

        value = 38

    @dataclass
    class Back:
        '''Background'''

        value = 48


# Color
class Color:
    '''Represents a Juneberry color'''

    class Custom:
        '''Custom Juneberry color'''

        @staticmethod
        def from_rgb(rgb: Tuple[R, G, B], mode: Union[Mode.Fore, Mode.Back]) -> str:
            '''Custom Juneberry color from RGB'''
            for component in rgb:
                if component > 255:
                    # RGB color component must not be more than 255
                    raise ValueError

            r = rgb[0]  # Red color component
            g = rgb[1]  # Green color component
            b = rgb[2]  # Blue color component

            return ansi256.format(mode=mode.value, r=r, g=g, b=b)

    class Default:
        '''Default Juneberry color'''

        class Fore:
            '''Default foreground Juneberry color'''

            mode = Mode.Fore.value
            # Foregrounds
            WHITE = ansi256.format(mode=mode, r=255, g=255, b=255)
            BLACK = ansi256.format(mode=mode, r=0, g=0, b=0)

            RED = ansi256.format(mode=mode, r=255, g=0, b=0)
            GREEN = ansi256.format(mode=mode, r=0, g=255, b=0)
            BLUE = ansi256.format(mode=mode, r=0, g=0, b=255)

        class Back:
            '''Default background Juneberry color'''

            mode = Mode.Back.value
            # Backgrounds
            WHITE = ansi256.format(mode=mode, r=255, g=255, b=255)
            BLACK = ansi256.format(mode=mode, r=0, g=0, b=0)

            RED = ansi256.format(mode=mode, r=255, g=0, b=0)
            GREEN = ansi256.format(mode=mode, r=0, g=255, b=0)
            BLUE = ansi256.format(mode=mode, r=0, g=0, b=255)


Colour = Color
