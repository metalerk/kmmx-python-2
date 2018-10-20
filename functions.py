# def suma(int: a, int: b) -> int:
# 	return a + b + c

# s = suma(4, 6)
# print(s)

# def suma(a, b):
# 	return a + b

def multiple_values():
	return 2, 3, 'hello'

result = multiple_values() # tupla

# a = result[0]
# b = result[1]
# c = result[2]

# a, b, c = result

# print(a)
# print(b)
# print(c)

def multiple_values(a, b, c):
	def pack_values(a, b, c):
		return [a, b, c]

	values = pack_values(a, b, c)

	return values

print(multiple_values(4, 5, 6))