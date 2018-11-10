import re

# https://pythex.org/

f = open('archivo', 'rw')
cad = f.read()
f.close()

matches = re.match(r'Error \d{3}', cad)
cad = re.sub(r'\d{3}', '300', cad)

f = open('archivo2', 'w')
f.write(cad)
f.close()
