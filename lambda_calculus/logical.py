from lambda_calculus.numbers import two, zero, one

if_then_else = lambda condition: lambda then_exp: lambda else_exp: condition(then_exp)(else_exp)

true = lambda then_exp: lambda else_exp: then_exp
false = lambda then_exp: lambda else_exp: else_exp

to_bool = lambda v: v(True)(False)

not_ = lambda boolean: boolean(false)(true)

or_ = lambda a: lambda b: a(a)(b)
and_ = lambda a: lambda b: a(b)(a)

result = not_(or_(and_(true)(false))(true))

is_zero = lambda n: n(lambda _: false)(true)
is_even = lambda n: n(not_)(true)
is_odd = lambda n: n(not_)(false)

# print(to_bool(result))
# print(to_bool(is_zero(zero)))
# print()
# print(to_bool(is_even(one)))
# print(to_bool(is_even(two)))
# print()
# print(to_bool(is_odd(one)))
# print(to_bool(is_odd(two)))
