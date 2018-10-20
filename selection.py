authorized_uid = (0, 1)

user1 = {
	'username': 'luis',
	'age': 26,
	'uid': 0
}

user2 = {
	'username': 'luis',
	'age': 26,
	'uid': 1
}

user3 = {
	'username': 'luis',
	'age': 26,
	'uid': 2
}

info_system = {
	'platform': 'Darwin x_64',
	'owner': 'pepito',
	'last_login': '18/10/2018 13:00:00'
}

def get_system_info(user):
	""" Authentication function """

	if user['uid'] in authorized_uid:
		return info_system

	elif user['uid'] == 2:
		print('Un DBA intenta acceder!!')
		return None

	else:
		return None

# dunder function
# print(get_system_info.__doc__)
assert get_system_info(user1) is not None
assert get_system_info(user2) is not None
assert get_system_info(user3) is None

