from colorama import init, Fore, Back, Style

init()

f = open('ips.txt', 'r')
for line in f.readlines():
	print('{red}[+]{reset} IP: {white}{ip}{reset}'.format(red=Fore.RED,
												   reset=Style.RESET_ALL,
												   white=Fore.YELLOW, 
												   ip=line.strip()))
f.close()