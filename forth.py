#!/usr/bin/python
# coding: utf-8


class ForthException(Exception):
    pass


class Forth(object):

    def __init__(self, statements):
        self._stack = []
        self._statements = statements
        self._current_statement = None

    def put(self):
        val = self._current_statement.split()[1]
        self._stack.append(eval(val))

    def pop(self):
        self._stack.pop()

    def add(self):
        a, b = self._stack.pop(), self._stack.pop()
        self._stack.append(a+b)

    def sub(self):
        a, b = self._stack.pop(), self._stack.pop()
        self._stack.append(a-b)

    def print_(self):
        return self._stack.pop()

    def run(self):
        for s in self._statements:
            if hasattr(self, s.split()[0]):
                method = getattr(self, s.split()[0])
                self._current_statement = s
                method()
            elif s.startswith('print'):
                # special hack for 'print' statement
                print self.print_()
            else:
                raise ForthException('Syntax error')


def eval_forth(file_name):
    with open(file_name, 'r') as f:
        source_code = f.readlines()

    source_code = map(lambda x: x.strip(), source_code)
    source_code = filter(lambda x: x if x[0]!='#' else False, source_code)

    forth = Forth(source_code)
    forth.run()


def main():
    eval_forth('example.frt')


if __name__ == '__main__':
    main()
