# [expression for value in iterables condition]
numbers=[x for x in range(1,11)]
print(numbers)

squares=[x**2 for x in range(1,11)]
print(squares)

evens=[x for x in range(1,11) if x%2==0]
print(evens)

evenodds=["0" if x %2==0 else "1" for x in range(1,11)]
print(evenodds)