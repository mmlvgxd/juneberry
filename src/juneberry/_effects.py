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
"""Juneberry effects"""

from ._type import _Effect

# ANSI
# 0: Escape Code
sgr = "\033[{0}m"

# ANSI Effects
_RESET = 0
_BOLD = 1
_FAINT = 2
_ITALIC = 3
_UNDERLINE = 4


class _Standart:
    """Juneberry Effects: Standart"""

    RESET: _Effect = sgr.format(_RESET)
    BOLD: _Effect = sgr.format(_BOLD)
    FAINT: _Effect = sgr.format(_FAINT)
    ITALIC: _Effect = sgr.format(_ITALIC)
    UNDERLINE: _Effect = sgr.format(_UNDERLINE)


class Effect:
    """
    Represents a Juneberry Effect

    Attributes:
        Standart (class): Juneberry Effect: Standart
    """

    Standart = _Standart
