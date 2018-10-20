user1 = {
	'username': 'pepito1',
	'age': 24,
	'id': 1,
}

user2 = {
	'username': 'juanito1',
	'age': 24,
	'id': 2,
}

user3 = {
	'username': 'pepito2',
	'age': 24,
	'id': 1,
}

user4 = {
	'username': 'pepito2',
	'age': 24,
	'id': 4,
}

role1 = {
	'role_id': 1,
	'role_name': 'dev',
	'stack': 'python',
}

role2 = {
	'role_id': 2,
	'role_name': 'dba',
	'stack': 'mongodb',
}

def merge_dicts(d1, d2):
	""" Merge dicts """

	aux = d1.copy()
	aux.update(d2)

	return aux

def get_user_role(user):
	#return merge_dicts(d1, d2)
	pass


#assert merge_dicts({'foo': 'bar'}, {'bar': 'baz'}) == {'foo': 'bar', 'bar': 'baz'}
assert get_user_role(user1)['role_name'] == 'dev'
assert get_user_role(user2)['stack'] == 'mongodb'
assert get_user_role(user3)['stack'] == 'python'
assert get_user_role(user4) is None
