""" A scaffold for the simple line-oriented text editor a la UNIX ed.
    The scaffold defines class Editor with a few methods for you to implement.
"""

__author__ = "Maria Garcia de la Banda, modified by Ben Di Stefano, Brendon Taylor and Alexey Ignatiev"
__docformat__ = 'reStructuredText'

from typing import List
from list_adt import ArrayList
import sys


class EditorError(Exception):
    """ Simple EditorError exception.
        Should be raised whenever an error occurs. """
    pass


class Editor:
    """ A simple line-oriented text editor.
        An instance of the Editor can be created and run like this:

        .. code-block:: python

            >>> ed = Editor()
            >>> ed.run()
    """

    def __init__(self) -> None:
        """ Object initialiser. """

        # here will be the text lines we are working with
        self.text_lines = ArrayList(40)

    def run(self) -> None:
        """ This is the frontend of the editor, which is basically an infinite
            loop iterating until the user executes the "quit" command.
            Feel free to improve!
        """

        okay = True
        while True:
            cmd = input('' if okay else '? ').strip()
            if cmd == 'quit':
                sys.exit(0)
            else:
                try:
                    self.execute_command(cmd)
                    okay = True
                except EditorError:
                    okay = False

    def execute_command(self, cmd: str) -> None:
        """ Run one command. """
        cmd = cmd.split()
        if cmd:
            if cmd[0] == 'read':
                self.read_filename(cmd[1])
            elif cmd[0] == 'print':
                self.print_num(line_num=cmd[1] if len(cmd) == 2 else None)
            elif cmd[0] == 'delete':
                self.delete_num(cmd[1])
            elif cmd[0] == 'insert':
                lines = []
                while True:
                    line = input()
                    if line == '.':
                        break
                    lines.append(line)
                self.insert_num(cmd[1], lines)
            elif cmd[0] == 'search':
                self.search_string(cmd[1], cmd[2] if len(cmd) == 3 else None)
            elif cmd[0] == 'undo':
                self.undo()
            else:
                raise EditorError('No such command')

    def read_filename(self, file_name):
        """ Read a file into self.text_lines. """
        pass

    def print_num(self, line_num: int = None) -> None:
        """ Print a line of text stored in self.text_lines specified by
            the input argument into standard output.
            If line_num is None, print all the lines.
        """
        to_be_printed = ""
        if line_num is None:
            for line in self.text_lines:
                to_be_printed += line + '\n'
        elif 0 < line_num <= self.text_lines.length:
            to_be_printed = self.text_lines[line_num - 1]
        elif line_num < 0:
            to_be_printed = self.text_lines[self.text_lines.length + line_num]
        else:
            raise EditorError()

        print(to_be_printed)

    def delete_num(self, line_num):
        """ Delete a line of text stored in self.text_lines specified by
            the input argument.
        """
        pass

    def insert_num(self, line_num: int, lines: List) -> None:
        """ Insert multiple lines at a given position. The position and
            the lines are specified as input arguments.
            :pre: lines is not None
            :pre: each line in lines is not None
            :pre: line_num cannot be 0
            :complexity best: O(1)*O(len(self)-index)
            :complexity worst: O(n)*O(len(self)-index) where n is the number of lines
        """
        if lines is None:
            raise EditorError

        for line in lines:
            temp_num = line_num
            if line is None:
                raise EditorError
            if line == ".":
                break
            elif 0 < line_num:
                self.text_lines.insert(line_num - 1, line)
                line_num += 1
            elif line_num < 0:
                self.text_lines.insert(self.text_lines.length + temp_num, line)
                temp_num += 1
            else:
                raise EditorError()


editor = Editor()
lines1 = ["Hello", "I am well. How are you?", "three", "four", "."]
lines2 = ["HELLO", "I AM WELL. HOW ARE YOU?", "."]
editor.insert_num(1, lines1)
editor.insert_num(-1, lines2)
editor.print_num()
exit()
