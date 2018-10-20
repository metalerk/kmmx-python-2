c = 0

while(c <= 10):
	print(c)
	c += 1


t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
t2 = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

f = True
c = 0
while(f):
	print(t[c])
	if t[c] == 5:
		break
	c += 1


# for(int i = 0; i <= t.length; i++)

for i in t:
	print(i)
	if i == 5:
		break

# i, j = (1, 1)
for i, j in zip(t, t2):
	print(i, j)
