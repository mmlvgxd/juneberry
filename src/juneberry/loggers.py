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
'''Juneberry loggers'''
from inspect import stack
from inspect import getmodule
from inspect import getmodulename

from sys import stdout
from .themes import default

from .themes import Theme
from .timestamps import Timestamp

from .colors import BOLD
from .colors import RESET
from .colors import ITALIC


class Logger:
    '''
    Represents a Juneberry logger

    Attributes:
        theme (Theme): Theme for the logger
    '''

    def __init__(self, *, theme: Theme = None) -> None:
        self.theme = theme

        if self.theme is None:
            self.theme = default

    def info(self, message: str) -> None:
        '''
        Confirmation that things are working as expected

        Parameters:
            message (str): A message to info
        '''
        timestamp = Timestamp(self.theme.timestamp)

        message = ITALIC + self.theme.message + message + RESET
        level = BOLD + self.theme.info + 'INFO' + RESET

        now = timestamp.new()

        frame = stack()[1]

        module = getmodule(frame[0])
        name = getmodulename(module.__file__)

        stdout.write(f'{RESET}[{now} {level}] ({module}:<{name}>) {message}\n')

    def warn(self, message: str) -> None:
        '''
        An indication that something unexpected happened,
        or indicative of some problem in the near future.
        The software is still working as expected.

        Parameters:
            message (str): A message to info
        '''
        timestamp = Timestamp(self.theme.timestamp)

        message = ITALIC + self.theme.message + message + RESET
        level = BOLD + self.theme.warn + 'WARN' + RESET

        now = timestamp.new()

        frame = stack()[1]

        module = getmodule(frame[0])
        name = getmodulename(module.__file__)

        stdout.write(f'{RESET}[{now} {level}] ({module}:<{name}>) {message}\n')

    def debug(self, message: str) -> None:
        '''
        Detailed information, typically of
        interest only when diagnosing problems

        Parameters:
            message (str): A message to info
        '''
        timestamp = Timestamp(self.theme.timestamp)

        message = ITALIC + self.theme.message + message + RESET
        level = BOLD + self.theme.debug + 'DEBUG' + RESET

        now = timestamp.new()

        frame = stack()[1]

        module = getmodule(frame[0])
        name = getmodulename(module.__file__)

        stdout.write(f'{RESET}[{now} {level}] ({module}:<{name}>) {message}\n')

    def error(self, message: str) -> None:
        '''
        Due to a more serious problem,
        the software has not been able to perform some function.

        Parameters:
            message (str): A message to info
        '''
        timestamp = Timestamp(self.theme.timestamp)

        message = ITALIC + self.theme.message + message + RESET
        level = BOLD + self.theme.error + 'ERROR' + RESET

        now = timestamp.new()

        frame = stack()[1]

        module = getmodule(frame[0])
        name = getmodulename(module.__file__)

        stdout.write(f'{RESET}[{now} {level}] ({module}:<{name}>) {message}\n')

    def fatal(self, message: str) -> None:
        '''
        A serious error, indicating that the program
        itself may be unable to continue running.

        Parameters:
            message (str): A message to info
        '''
        timestamp = Timestamp(self.theme.timestamp)

        message = ITALIC + self.theme.message + message + RESET
        level = BOLD + self.theme.fatal + 'FATAL' + RESET

        now = timestamp.new()

        frame = stack()[1]

        module = getmodule(frame[0])
        name = getmodulename(module.__file__)

        stdout.write(f'{RESET}[{now} {level}] ({module}:<{name}>) {message}\n')
