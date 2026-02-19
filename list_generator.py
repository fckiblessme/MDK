import random
n = 18
def create_list(count):
	return [random.randint(5, n * 100) for i in range(count)]
numbers = create_list(5)
print(numbers)
