def generador(max):
	for x in range(max):
		yield x


# for x in generador(10):
# 	print(x)

print(generador(10))
g = generador(10)
print(next(g))
print(next(g))
print(g.__next__())
