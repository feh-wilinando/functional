from functools import wraps
from collections.abc import Container
from abc import abstractmethod, ABC


class Either(ABC):
    @abstractmethod
    def is_left(self):
        """
        >>> result = Left(value=10)
        >>> result.is_right()
        False
        >>> result.is_left()
        True
        >>> result.value
        10
        """
        pass

    @abstractmethod
    def is_right(self):
        """
        >>> result = Right(value=10)
        >>> result.is_right()
        True
        >>> result.is_left()
        False
        >>> result.value
        10
        """
        pass

    @property
    @abstractmethod
    def value(self):
        pass

    def __contains__(self, item):
        return item in self.value if isinstance(self.value, Container) else item == self.value

    def map(self, func):
        """
        >>> right_value = Right(value=12)
        >>> right_value.value
        12
        >>> new_right_value = right_value.map(lambda x: x * 2)
        >>> new_right_value.is_right()
        True
        >>> new_right_value.value
        24
        >>> left_value = Left(value=12)
        >>> left_value.value
        12
        >>> new_left_value = left_value.map(lambda x: x * 2)
        >>> new_left_value.is_right()
        False
        >>> left_value == new_left_value
        True
        """
        if self.is_right():
            return either()(func)(self.value)

        return self


class Left(Either):

    def __init__(self, value):
        self._value = value

    def is_left(self):
        return True

    def is_right(self):
        return False

    @property
    def value(self):
        return self._value


class Right(Either):
    def __init__(self, value):
        self._value = value

    def is_left(self):
        return False

    def is_right(self):
        return True

    @property
    def value(self):
        return self._value


def either(*, expected_type=None):
    """
    >>> from numbers import  Number
    >>> @either(Number)
    ... def divide(a, b):
    ...     return a / b
    >>> either_of_4_div_2 = divide(4, 2)
    >>> isinstance(either_of_4_div_2, Either)
    True
    >>> either_of_4_div_2.is_right()
    True
    >>> either_of_4_div_2.value
    2.0
    >>> either_of_0_div_1 = divide(1, 0)
    >>> isinstance(either_of_0_div_1, Either)
    True
    >>> either_of_0_div_1.is_right()
    False
    >>> either_of_0_div_1.value # doctest: +ELLIPSIS
    ZeroDivisionError(...)
    """

    def closure(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                return Left(value=e)
            else:
                return Right(value=result) if expected_type is None else \
                        Right(value=result) if isinstance(result, expected_type) else \
                        Left(value=result)

        return inner

    return closure
