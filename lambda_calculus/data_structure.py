from lambda_calculus.arithmetic import four, three
from lambda_calculus.base import konstant
from lambda_calculus.logical import to_bool, true, false
from lambda_calculus.numbers import to_int, one, two

pair = lambda first: lambda second: lambda f: f(first)(second)

fst = lambda some_pair: some_pair(true)
snd = lambda some_pair: some_pair(false)

# print(to_int(fst(pair(one)(two))))
# print(to_int(snd(pair(one)(two))))

is_empty = snd

nil = pair(true)(true)

# print(to_bool(is_empty(nil)))

prepend = lambda item: lambda rest: pair(false)(pair(item)(rest))

head = lambda lst: fst(snd(lst))
tail = lambda lst: snd(snd(lst))

numbers = prepend(one)(prepend(two)(prepend(three)(prepend(four)(nil))))

print(to_int(head(tail((tail((tail(numbers))))))))
