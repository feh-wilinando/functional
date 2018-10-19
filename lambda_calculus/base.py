identity = lambda a: a

konstant = lambda a: lambda b: a

konstant_identity = lambda a: konstant(identity)(a)

apply = lambda f: f(f)

head = lambda a: lambda b: a

tail = lambda a: lambda b: b

flip = lambda f: lambda a: lambda b: f(b)(a)
