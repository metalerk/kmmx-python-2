from pprint import pprint

# Variables

# int
integer = 4
print(integer)
print(type(integer))

print('============')

# float
float_val = 3.0
print(float_val)
print(type(float_val))


print('============')

# str
text = 'hello_world'
print(text)
print(type(text))

print('============')

# bool
boolean_true = True
boolean_false = False

print(boolean_true)
print(boolean_false)
print(type(boolean_true))

print('============')

# list
list_type = list()
list_type = []

list_type = [integer, float_val, text, boolean_true, [1, True, []],]
print(list_type)
print(type(list_type))

print('============')

# tuple
tuple_type = tuple()
tuple_type = 1,

tuple_type = (integer, float_val, text, boolean_true, (1, True, ()),)
print(tuple_type)

print('============')

# dict
d = dict()
d = {}

gamer = {
	'username': 'pepito1',
	'age': 26,
	'amigos': [],
	'logros': {
		'logro1': True,
		'logro2': False, # trailing comma
	}, # trailing comma
}

pprint(gamer, indent=4)

print('============')

# set
s = set()
s = {integer, integer, float_val, text, boolean_true,}

print(s)

print(set([1,2,2,3,4]))

print('============================================\n')

# None
null = None


# Conversiones

int_to_float = float(integer)
print(int_to_float)

float_to_int = int(float_val)
print(float_to_int)

int_to_str = str(integer)
print(int_to_str)

str_to_int = int('2')
print(str_to_int)

list_to_tuple = tuple(list_type)
print(list_to_tuple)

l = [1, 2, 2, 2, 3, 3, 4, 5]
print(l)
list_to_set = set(l)
print(list_to_set)

non_duplicated_elem = list(list_to_set)
list_comprehension = [x for x in set(l)]

print(list_comprehension)

print(non_duplicated_elem)

########################

e = gamer['logros']['logro1']
print(e)

c = [integer, float_val, text, boolean_true, [1, True, [False]],]
c[0] = 5
e = c[4][2][0]
print(e)


print(1 + 3)
print(9 - 3)
print(9 * 3)
print(9 / 3)
print(9 // 2)
print(6 ** 2)
print(9 % 2)

counter = 7

#counter = counter + 1
counter += 1
print(counter)

counter -= 1
print(counter)

counter *= 3
print(counter)

counter /= 3
print(counter)


print(1 == 1.0) # True
print(1 == '1') # False
print(1 != 2) # True
print( not(1 != 1.0) ) # True

print('==============')

age = 21

print( (age <= 6) or (age > 18 )  )

l = [1, 2, 3, 4]
l[1] = 0
print(l)

gamer['age'] = 27
print(gamer)

c = {1, 2, 3, 4, 5, 6, 7 ,8, 9, 0}
c2 = {45, 5, 6, 12}
print(c.isdisjoint(c2))

print(c & c2)

