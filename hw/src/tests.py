import types

import pytest
import fibonachi


def test_numbers():
    assert [0, 1, 1, 2] == list(fibonachi.fib(4))
    assert [0, 1, 1, 2, 3, 5] == list(fibonachi.fib(6))
    assert [0, 1, 1, 2, 3, 5, 8, 13] == list(fibonachi.fib(8))


def test_lazy():
    assert types.GeneratorType == type(fibonachi.fib(5))
