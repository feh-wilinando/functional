to_int = lambda n: n(lambda i: i + 1)(0)

zero = lambda f: lambda x: x
one = lambda f: lambda x: f(x)
two = lambda f: lambda x: f(f(x))

assert to_int(zero) == 0
assert to_int(one) == 1
assert to_int(two) == 2