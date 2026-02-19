import random
n = 18
def create_list(count):
	result = []
	i = 0
	while i < count:
		result.append(random.randint(5, n * 100))
		i = i + 1
	return result
numbers = create_list(5)
print(numbers)
