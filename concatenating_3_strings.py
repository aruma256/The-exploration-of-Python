import inspect
from typing import Callable
import unittest


class _Functions:

    @staticmethod
    def the_obvious_way(a: str, b: str, c: str) -> str:
        """
        'The Zen of Python' says:
        "There should be one-- and preferably only one --obvious way to do it."
        https://www.python.org/dev/peps/pep-0020/
        """
        return a + b + c

    @staticmethod
    def wasteful_string_concatenation(a: str, b: str, c: str) -> str:
        res = ''
        res += a
        res += b
        res += c
        return res

    @staticmethod
    def join_empty_string(a: str, b: str, c: str) -> str:
        """https://docs.python.org/ja/3/library/stdtypes.html#str.join
        """
        return ''.join((a, b, c))

    @staticmethod
    def join_b(a: str, b: str, c: str) -> str:
        """https://docs.python.org/ja/3/library/stdtypes.html#str.join
        """
        return b.join((a, c))

    @staticmethod
    def join_using_chain(a: str, b: str, c: str) -> str:
        """https://docs.python.org/ja/3/library/itertools.html#itertools.chain
        """
        import itertools
        return ''.join(itertools.chain(a, b, c))

    @staticmethod
    def join_using_deque(a: str, b: str, c: str) -> str:
        """https://docs.python.org/ja/3/library/collections.html#collections.deque
        """
        import collections
        q = collections.deque()
        q.extend(a)
        q.extend(b)
        q.extend(c)
        return ''.join(q)

    @staticmethod
    def format_omitted(a: str, b: str, c: str) -> str:
        """https://docs.python.org/3/library/stdtypes.html#str.format
        """
        return '{}{}{}'.format(a, b, c)

    @staticmethod
    def format_position(a: str, b: str, c: str) -> str:
        """https://docs.python.org/3/library/string.html#formatstrings
        """
        return '{0}{1}{2}'.format(a, b, c)

    @staticmethod
    def format_name(a: str, b: str, c: str) -> str:
        """https://docs.python.org/3/library/string.html#formatstrings
        """
        return '{a}{b}{c}'.format(a=a, b=b, c=c)

    @staticmethod
    def format_f_strings(a: str, b: str, c: str) -> str:
        """https://docs.python.org/3/reference/lexical_analysis.html#f-strings
        """
        return f'{a}{b}{c}'

    @staticmethod
    def functools_reduce(a: str, b: str, c: str) -> str:
        """https://docs.python.org/3/library/functools.html#functools.reduce
        """
        import functools
        import operator
        return functools.reduce(operator.add, (a, b, c))

    @staticmethod
    def io_write(a: str, b: str, c: str) -> str:
        """https://docs.python.org/ja/3/library/io.html#io.StringIO
        """
        import io
        output = io.StringIO()
        output.write(a)
        output.write(b)
        output.write(c)
        return output.getvalue()

    @staticmethod
    def io_print(a: str, b: str, c: str) -> str:
        """https://docs.python.org/ja/3/library/io.html#io.StringIO
        """
        import io
        output = io.StringIO()
        print(a, b, c, sep='', end='', file=output)
        return output.getvalue()


if __name__ == '__main__':

    class _TestCase(unittest.TestCase):
        pass

    def create_test(func: Callable[[str, str, str], str]) -> Callable[[unittest.TestCase], None]:
        def _test_func(self: unittest.TestCase) -> None:
            self.assertEqual("Python", func("Py", "th", "on"))
            self.assertEqual("", func("", "", ""))
            self.assertEqual("cBa", func("c", "B", "a"))
        return _test_func

    for name, func in inspect.getmembers(_Functions, inspect.isfunction):
        setattr(_TestCase, 'test_' + name, create_test(func))

    unittest.main()
