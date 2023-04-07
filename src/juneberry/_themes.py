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
"""Juneberry themes"""

from ._colors import Color
from ._effects import Effect

from ._modules import Module
from ._messages import Message
from ._timestamps import Timestamp

from ._type import _Color


class Theme:
    """
    Represents a Juneberry theme

    Attributes:
        info (_Color): Color for info level
        warn (_Color): Color for warn level
        debug (_Color): Color for deubg level
        error (_Color): Color for error level
        fatal (_Color): Color for fatal level
        module (_Color): Color for module
        timestamp (_Color): Color for timestamp
        message (_Color): Color for message
    """

    def __init__(
        self,
        info: _Color,
        warn: _Color,
        debug: _Color,
        error: _Color,
        fatal: _Color,
        module: Module,
        message: Message,
        timestamp: Timestamp,
    ) -> None:
        self.info = info
        self.warn = warn
        self.debug = debug
        self.error = error
        self.fatal = fatal
        self.module = module
        self.message = message
        self.timestamp = timestamp


# Default theme
default_theme = Theme(
    Color.Standart.WHITE,  # Info
    Color.Standart.BLUE,  # Warn
    Color.Standart.CYAN,  # Debug
    Color.Standart.MAGENTA,  # Error
    Color.Standart.RED,  # Fatal
    Module(Color.Standart.YELLOW, Effect.Standart.UNDERLINE),
    Message(Color.Standart.GREEN, Effect.Standart.RESET),
    Timestamp(Color.Standart.GREEN, Effect.Standart.RESET),
)
