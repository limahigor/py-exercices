import os
import argparse

def pick_command(string):
	command = []
	pos = [i for i in range(len(string)) if string[i] == '[' or string[i] == ']'] #pega a posição dos [ ] 
																				  #a string
	if(len(pos) % 2 == 0): #se o numero de [ ] não for par, sintaxe invalida
		i = 0
		while(i < len(pos)): #verifica se cada '[' forma seu par ']'. se não, sintaxe invalida
			j = i+1
			string_temp = ''
			if string[pos[i]] == '[':
				if string[pos[j]] == ']':
					n = pos[i+1]
					while(n < pos[j]): #pega o conteudo das []
						string_temp = string_temp + string[n]
						n += 1
					command.append(string_temp)
					i = j + 1;
				else:
					exit('Sintaxe invalida!\nren --help para mais informações')
			else:
				exit('Sintaxe invalida!\nren --help para mais informações')
	else:
		exit('Sintaxe invalida!\nren --help para mais informações')

	return command

def main():
	parser = argparse.ArgumentParser(prog='ren',
									 usage='%(prog)s [ARQ] [OPTIONS] [NOME]\n%(prog)s --help para mais informações',
									 description='Renomeia arquivos')

	parser.add_argument('name',
						type=str,
						metavar='DIR/ARQ',
						nargs='*')

	parser.add_argument('dest',
						type=str,
						metavar='NOME',)

	parser.add_argument('-m',
						action='store_true',
						help='Renomeia vários arquivos ao mesmo tempo')

	args = parser.parse_args()

	caminho = os.path.dirname(args.name[0])

	print(args.name)
	print()
	print(args.dest)

	if os.path.isdir(caminho):
		caminho = os.path.abspath(caminho)
		command = pick_command(args.dest)
	else:
		parser.exit('Diretorio inexistente')

if __name__ == "__main__":
	main()