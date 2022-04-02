""" A scaffold for the simple line-oriented text editor a la UNIX ed.
    The scaffold defines class Editor with a few methods for you to implement.
"""

__author__ = "Maria Garcia de la Banda, modified by Ben Di Stefano, Brendon Taylor and Alexey Ignatiev"
__docformat__ = 'reStructuredText'

from typing import List
from list_adt import ArrayList
from stack_adt import ArrayStack
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
        self.command_history = ArrayStack(40)

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
                self.print_num(line_num=int(cmd[1]) if len(cmd) >= 2 else None)
            elif cmd[0] == 'delete':
                record = [cmd[0],
                          [self.text_lines[int(cmd[1]) - 1]] if len(cmd) >= 2 else [line for line in self.text_lines],
                          int(cmd[1]) if len(cmd) >= 2 else 1]
                if self.delete_num(line_num=int(cmd[1]) if len(cmd) >= 2 else None):
                    self.command_history.push(record)
            elif cmd[0] == 'insert':
                lines = []
                while True:
                    line = input()
                    if line == '.':
                        break
                    lines.append(line)
                record = [cmd[0], int(cmd[1]) if len(cmd) >= 2 else None, len(lines)]
                if self.insert_num(int(cmd[1]) if len(cmd) >= 2 else None, lines):
                    self.command_history.push(record)
            elif cmd[0] == 'search':
                self.search_string(cmd[1], int(cmd[2]) if len(cmd) == 3 else None)
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

    def print_num(self, line_num: int = None):
        """ Print a line of text stored in self.text_lines specified by
            the input argument into standard output.
            If line_num is None, print all the lines.
        """
        if type(line_num) is str:
            line_num = int(line_num)

        to_be_printed = ""
        if line_num is None:
            for line in self.text_lines:
                to_be_printed += line + '\n'
            to_be_printed = to_be_printed[:len(to_be_printed) - 1 ]
        elif 0 < line_num <= self.text_lines.length:
            to_be_printed = self.text_lines[line_num - 1]
        elif line_num < 0:
            to_be_printed = self.text_lines[self.text_lines.length + line_num]
        else:
            raise EditorError()

        print(to_be_printed)

    def delete_num(self, line_num: int) -> bool:
        """ Delete a line of text stored in self.text_lines specified by
            the input argument.
        """
        if type(line_num) is str:
            line_num = int(line_num)

        success = False
        if line_num is None:
            self.text_lines.clear()
            success = True
        elif 0 < int(line_num) <= self.text_lines.length:
            self.text_lines.delete_at_index(line_num - 1)
            success = True
        elif int(line_num) < 0:
            self.text_lines.delete_at_index(self.text_lines.length + line_num)
            success = True
        elif int(line_num) == 0 or int(line_num) > self.text_lines.length:
            raise EditorError()

        return success

    def insert_num(self, line_num: int, lines: List) -> bool:
        """ Insert multiple lines at a given position. The position and
            the lines are specified as input arguments.
            :pre: lines is not None
            :pre: each line in lines is not None
            :pre: line_num cannot be 0
            :complexity best: O(1)*O(len(self)-index)
            :complexity worst: O(n)*O(len(self)-index) where n is the number of lines
        """
        success = False

        if lines is None:
            raise EditorError
        if type(line_num) is str:
            line_num = int(line_num)

        for line in lines:
            temp_num = line_num
            if line is None:
                raise EditorError
            if line == ".":
                success = True
                break
            elif 0 < line_num:
                self.text_lines.insert(line_num - 1, line)
                line_num += 1
                success = True
            elif line_num < 0:
                self.text_lines.insert(self.text_lines.length + temp_num, line)
                temp_num += 1
                success = True
            else:
                raise EditorError()

        return success

    def search_string(self, query: str, replace_with: str = None) -> None:
        """ Search a string in the current text lines.
            Print all text lines that contain the target query if
            no second argument is given. Otherwise, replace the first
            occurrence of the input string with the second argument.
            Make sure you use self.print_num() for printing and
            self.delete_num() + self.insert_num() for replacement.
        """
        if query is None:
            raise EditorError
        elif replace_with is None:
            found_lines = ""
            for line in self.text_lines:
                for j in range(len(line) - 1):
                    if line[j:j + len(query)] == query:
                        found_lines += line + "\n"
                        break
            found_lines = found_lines[:len(found_lines) - 1]
            print(found_lines)
        else:
            for i in range(self.text_lines.length):
                line = self.text_lines[i]
                for j in range(len(line) - 1):
                    if line[j:j + len(query)] == query:
                        new_line = line[:j] + replace_with + line[j + len(query):]
                        self.delete_num(i + 1)
                        self.insert_num(i + 1, [new_line])
                        break
            self.print_num()

    def undo(self) -> None:
        """ Undo the previous operation. """
        if len(self.command_history) > 0:
            last_command = self.command_history.pop()
            if last_command[0] == "delete":
                self.insert_num(last_command[2], last_command[1])

            elif last_command[0] == "insert" and last_command[1] is not None:
                for _ in range(last_command[2]):
                    self.delete_num(last_command[1])


editor = Editor()
editor.read_filename("small.txt")
query = "t"
editor.search_string(query, "REPLACEMENT")
exit()
