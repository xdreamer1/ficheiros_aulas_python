import os

inscritos = ['Maria Silva Advogada', 'Vitor Silva Professor']

with open('inscritos.txt', 'w', newline='') as file:
	for line in inscritos:
		file.write(line + os.linesep)