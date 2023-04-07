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
"""Juneberry colors"""

from ._type import _Color

# ANSI
# 0: Escape Code
sgr = "\033[{0}m"

# 0: Mode, 1: Red, 2: Green, 3: Blue
a24 = "{0};2;{1};{2};{3}"

# ANSI Mode
FORE = 38
BACK = 48


class _Converter:
    """Juneberry Colors: Converters"""

    @staticmethod
    def from_rgb(red: int, green: int, blue: int) -> _Color:
        """
        Color from RGB

        Parameters:
            rgb (tuple[R, G, B]): RGB to use
        """
        rgb = red, green, blue

        # RGB Component must not be over 255
        for component in rgb:
            ...
            if component > 255:
                raise ValueError

        return sgr.format(a24.format(FORE, red, green, blue))


class _Standart:
    """Juneberry Colors: Standart"""

    WHITE: _Color = _Converter.from_rgb(255, 255, 255)
    BLACK: _Color = _Converter.from_rgb(0, 0, 0)

    RED: _Color = _Converter.from_rgb(255, 0, 0)
    GREEN: _Color = _Converter.from_rgb(0, 255, 0)
    BLUE: _Color = _Converter.from_rgb(0, 0, 255)

    YELLOW: _Color = _Converter.from_rgb(255, 255, 0)
    CYAN: _Color = _Converter.from_rgb(0, 255, 255)
    MAGENTA: _Color = _Converter.from_rgb(255, 0, 255)


class Color:
    """
    Represents a Juneberry Color

    Attributes:
        Converters (class): Juneberry Colors: Converters
        Standart (class): Juneberry Colors: Standart
    """

    Standart = _Standart
    Converters = _Converter
