def square(num):
    return num * num

square(2) # => 4

square_lambda = lambda num: num * num

assert square(4) == square_lambda(4)

domain = [1, 2, 3, 4, 5]

# f(x) = x * 2
our_range = map(lambda num: num * 2, domain)

print("hello")
print("hello")