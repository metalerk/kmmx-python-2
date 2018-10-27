# l = []
# for x in range(21):
# 	if x % 2 == 0:
# 		l.append(x)

# print(l)

def generador(maxn):
	for x in range(maxn):
		yield x

l = [x for x in generador(15) if x % 2 == 0]
print(l)

l = [1,2,3,4,5]
