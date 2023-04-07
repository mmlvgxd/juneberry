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
"""Juneberry loggers"""

from ._effects import Effect

from ._themes import default_theme

from ._themes import Theme
from ._levels import Level

from ._levels import INFO
from ._levels import WARN
from ._levels import DEBUG
from ._levels import ERROR
from ._levels import FATAL


class Logger:
    """
    Represents a Juneberry logger

    Attributes:
        theme (Theme): Theme for the logger
    """

    def __init__(self, *, theme: Theme = None) -> None:
        self.__theme = theme

        if self.__theme is None:
            self.__theme = default_theme

    def _log(self, level: Level, message: str, scope: tuple) -> None:
        _level = (
            self.__theme.__getattribute__(level.name)
            + Effect.Standart.BOLD
            + level.name.upper()
            + Effect.Standart.RESET
        )
        _message = (
            self.__theme.message.effect
            + self.__theme.message.color
            + message
            + Effect.Standart.RESET
        )
        _timestamp = (
            self.__theme.timestamp.effect
            + self.__theme.timestamp.color
            + self.__theme.timestamp.get()
            + Effect.Standart.RESET
        )
        scope = self.__theme.module.get()
        _module = (
            self.__theme.module.effect
            + self.__theme.module.color
            + f"{scope[0]}:<{scope[1]}>"
            + Effect.Standart.RESET
        )

        struct = f"[{_timestamp} {_level}] ({_module}) {_message}"

        print(struct)

    def info(self, message: str) -> None:
        """
        Confirmation that things are working as expected

        Parameters:
            message (str): A message to info
        """
        self._log(INFO, message, self.__theme.timestamp.get())

    def warn(self, message: str) -> None:
        """
        An indication that something unexpected happened,
        or indicative of some problem in the near future.
        The software is still working as expected.

        Parameters:
            message (str): A message to warn
        """
        self._log(WARN, message, self.__theme.timestamp.get())

    def debug(self, message: str) -> None:
        """
        Detailed information, typically of
        interest only when diagnosing problems

        Parameters:
            message (str): A message to debug
        """
        self._log(DEBUG, message, self.__theme.timestamp.get())

    def error(self, message: str) -> None:
        """
        Due to a more serious problem,
        the software has not been able to perform some function.

        Parameters:
            message (str): A message to error
        """
        self._log(ERROR, message, self.__theme.timestamp.get())

    def fatal(self, message: str) -> None:
        """
        A serious error, indicating that the program
        itself may be unable to continue running.

        Parameters:
            message (str): A message to fatal
        """
        self._log(FATAL, message, self.__theme.timestamp.get())
