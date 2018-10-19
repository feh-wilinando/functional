from lambda_calculus.numbers import two, one, to_int

add = lambda m: lambda n: lambda f: lambda x: m(f)(n(f)(x))
mul = lambda m: lambda n: lambda f: lambda x: m(n(f))(x)
power = lambda m: lambda n: lambda f: lambda x: m(n)(f)(x)


three = add(two)(one)

four = add(three)(one)

twelve = mul(three)(four)

six = add(four)(two)
eight = power(two)(three)

# print(to_int(three))
# print(to_int(twelve))
# print(to_int(eight))
# print(to_int(six))
