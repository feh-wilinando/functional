from functools import wraps

from monads import tryable


class Just:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    def bind(self, func):
        return Maybe(func(self.value))


class Nothing:

    @property
    def value(self):
        return None

    def bind(self, func):
        return Nothing()


class Maybe:
    """
    >>> n = Maybe(None).bind(lambda a: a + 1).bind(lambda a: a + 1)
    >>> n # doctest: +ELLIPSIS
    <maybe.Nothing object at ...>
    >>> n.value is None
    True
    >>> j = Maybe(1).bind(lambda a: a + 1)
    >>> j # doctest: +ELLIPSIS
    <maybe.Just object at ...>
    >>> j.value
    2
    """
    def __new__(cls, value):
        return Just(value) if value else Nothing()

