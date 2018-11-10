# def foo(*args, **kwargs):
# 	print(args)
# 	print('=======')
# 	print(kwargs)

# params = {
# 	'param1': '1',
# 	'param2': 2
# }

# foo('hola', 'adios', **params)

def debug(func):
	def wrapper(*args, **kwargs):
		print('=================')
		print('El nombre de la función es {}'.format(func.__name__))
		print('=================')
		# print(f'{func.__name__}')

		return func(*args, **kwargs)
	return wrapper

@debug
def suma(a, b):
	return a + b

print(suma(1, 2))
