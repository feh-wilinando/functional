from abc import abstractmethod
from functools import wraps


def tryable(func):
    """
    >>> @tryable
    ... def even(value):
    ...     if value % 2 == 0:
    ...         return value * 2
    ...     raise ZeroDivisionError('blaaa')
    >>> result = even(4)
    >>> result.is_success
    True
    >>> result.value
    8
    >>> result_fail = even(3)
    >>> result_fail.is_success
    False
    >>> result_fail.value # doctest: +ELLIPSIS
    ZeroDivisionError(...)
    """

    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return Success(value=func(*args, **kwargs))
        except Exception as e:
            return Fail(value=e)

    return inner


class Try:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @property
    @abstractmethod
    def is_success(self):
        pass


class Fail(Try):
    @property
    def is_success(self):
        return False


class Success(Try):
    @property
    def is_success(self):
        return True
