# coding: utf-8

import unittest
from functools import wraps


def args_type_ckecker(*checker_args):

    def decorator(func):
        @wraps(func)
        def wrapper(*func_args):
            if len(checker_args) != len(func_args):
                raise TypeError('Incorrect arguments number. Expected {}, given - {} arguments'.format(len(checker_args), len(func_args)))

            for i,arg in enumerate(func_args):
                if type(arg) is not checker_args[i]:
                    raise TypeError('Incorrect argument type in {} position. Expected "{}", but get "{}"'.format(i+1, checker_args[i].__name__, type(arg).__name__))

            return func(*func_args)
        return wrapper

    return decorator




class ArgsTypeChecker(unittest.TestCase):

    def setUp(self):
        @args_type_ckecker(int, int, str)
        def test(x, y, z):
            return x + y + int(z)

        self.test_func = test

    def test_work_fine(self):
        self.assertEqual(self.test_func(1, 2, '3'), 6)

    def test_incorrect_arguments_number(self):
        self.assertRaises(TypeError, self.test_func, (1,2,3))

    def test_incorrect_argument_type_1(self):
        self.assertRaises(TypeError, self.test_func, (1,2))

    def test_incorrect_argument_type_2(self):
        self.assertRaises(TypeError, self.test_func, (1,2,3,4))


if __name__ == '__main__':
    unittest.main()
