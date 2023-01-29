from functools import reduce
domain = [1, 2, 3, 4, 5]

#map allows us to take a list and process each item in that list with teh function below and whatever the return value is on below function, we will return in a list
#that is the same size as the original list. 
# f(x) = x * 2
our_range = map(lambda num: num * 2, domain) #mapping an algebraic function over a set the collection (domain)
print(list(our_range))

#filter is same as map, and then filter it
evens = filter(lambda num: num % 2 == 0, domain) #take the numbers in the domain collection and put in the num % 2 == 0, if returned true, then it will print it in evens list
print(list(evens))

#packaged from functools, take an iterable and starting point accumulator and work way down to a single item. Sum is an example of this
the_sum = reduce(lambda acc, num: acc + num, domain, 0)  
print(the_sum)

words = ['Boss', 'a', 'Alfred', 'fig', 'Daemon', 'dig']
print("Sorting by default")
print(sorted(words))

print("Sorting with a lambda key")
print(sorted(words, key=lambda s: s.lower()))

print("Sorting with a method")
words.sort(key=str.lower, reverse=True)
print(words)