"""
Gnumeric-py: Reading and writing gnumeric files with python
Copyright (C) 2017 Michael Lipschultz

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""


class DuplicateTitleException(Exception):
    """
    A workbook cannot contain multiple sheets with the same name/title.
    """

    def __init__(self, msg):
        super().__init__(msg)


class WrongWorkbookException(Exception):
    """
    A sheet or cell from one workbook being using in another workbook.
    """

    def __init__(self, msg):
        super().__init__(msg)


class UnsupportedOperationException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class UnrecognizedCellTypeException(Exception):
    """
    The type of cell cannot be determined.
    """

    def __init__(self, msg):
        super().__init__(msg)
