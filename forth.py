#!/usr/bin/python
# coding: utf-8


class ForthException(Exception):
    pass


class Forth(object):

    def __init__(self, statements):
        self.stack = []   # _ not for this case
        self.statements = statements
        self.current_statement = None

    def put(self):
        val = self._current_statement.split()[1] # put "I will kill you interpreter"
        self._stack.append(eval(val))  # you need to remove ''"" from string values

    def pop(self):
        self._stack.pop()

    def add(self):
        a, b = self._stack.pop(), self._stack.pop() # are you sure about tuple items evaluation order?
        self._stack.append(a+b)

    def sub(self):
        a, b = self._stack.pop(), self._stack.pop()
        self._stack.append(a-b)

    def print_(self):
        print self._stack.pop()

    def run(self):
        for s in self._statements:
            if hasattr(self, s.split()[0]):
                method = getattr(self, s.split()[0])  # what is "run 1" would be in frt file?
                self._current_statement = s  # ugly way of passing parameter to method()
                method() # << method(s)
            elif s.startswith('print'):
                # special hack for 'print' statement
                print self.print_()
            else:
                raise ForthException('Syntax error') # in this case should also be used for stack


def eval_forth(file_name):
    with open(file_name, 'r') as f:
        source_code = f.readlines()

    source_code = map(lambda x: x.strip(), source_code)
    source_code = filter(lambda x: x if x[0]!='#' else False, source_code)

    Forth(source_code).run() # this isn't a class :)


def main():
    eval_forth('example.frt') # should get file name from command line


if __name__ == '__main__':
    main()
