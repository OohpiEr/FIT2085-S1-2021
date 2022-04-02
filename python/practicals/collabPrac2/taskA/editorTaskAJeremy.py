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
                self.delete_num(line_num=cmd[1] if len(cmd) == 2 else None)
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

    def read_filename(self, file_name: str) -> None:
        """ Read a file into self.text_lines. """
        try:
            with open(file_name) as file:
                for line in file:
                    self.text_lines.append(line.rstrip())
        except FileNotFoundError:
            raise EditorError()

    def print_num(self, line_num):
        """ Print a line of text stored in self.text_lines specified by
            the input argument into standard output.
            If line_num is None, print all the lines.
        """
        print(self.text_lines)

    def delete_num(self, line_num: str) -> None:
        """ Delete a line of text stored in self.text_lines specified by
            the input argument.
        """
        if line_num is None:
            self.text_lines.clear()
        elif 0 < int(line_num) <= self.text_lines.length:
            self.text_lines.delete_at_index(line_num - 1)
        elif int(line_num) < 0:
            self.text_lines.delete_at_index(self.text_lines.length + line_num)
        elif int(line_num) == 0 or int(line_num) > self.text_lines.length:
            raise EditorError()

    def insert_num(self, line_num, lines):
        """ Insert multiple lines at a given position. The position and
            the lines are specified as input arguments.
        """
        pass


editor = Editor()
editor.read_filename("small.txt")
editor.delete_num(-1)
print(editor.text_lines)
editor = Editor()
editor.read_filename("small2.txt")
editor.delete_num(2)
editor.delete_num(2)
print(editor.text_lines)
editor = Editor()
editor.read_filename("small3.txt")
editor.delete_num(4)
print(editor.text_lines)
editor = Editor()
editor.read_filename("small4.txt")
editor.delete_num(1)
editor.delete_num(3)
editor.delete_num(3)
print(editor.text_lines)

exit()
