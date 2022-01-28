import argparse
import cpf_lib as cpft

def main():
	# Definindo os parsers e seus argumentos
	parser = argparse.ArgumentParser(prog="cpftools",
									 usage="%(prog)s [OPTIONS] [ARGUMENTS]\n%(prog)s --help para mais informações\n\n",
	                                 description="Gera e verifica CPF's e CNPJ's",
	                                 epilog="Caso '-i': Cada CPF/CNPJ deve ocupar uma linha no arquivo")

	subparser = parser.add_subparsers(dest="command")

	check = subparser.add_parser("check",
								 help="Verifica se um cpf é valido")

	gen = subparser.add_parser("gen",
									help="Gera CPF's/CNPJ's")

	check.add_argument("-i", "--input",
						help="Pega CPF's de um arquivo",
						action="store_true")

	check.add_argument("name",
		                type=str,
						help="Pega o CPF/Caminho do arquivo",
						metavar='[CPF/CNPJ]')

	gen.add_argument("n",
					 type=int,
					 help="Quantidade de CPF's/CNPJ a ser gerados",
					 metavar="N",
					 nargs="?",
					 default=1)

	args = parser.parse_args()

	if args.command == None:
		parser.exit("cpftools [OPTIONS] [ARGUMENTS]\ncpftools --help para mais informações");
	elif args.command == 'check':
		if args.input: #Pegando CPF de arquvivos
			try:
				arq = open(args.name, 'r')
				cpf = arq.readlines()
				for i in cpf:
					i = i.rstrip('\n')
					if cpft.verifica_cpf(i):
						print(f"{i}: Válido")
					else:
						print(f"{i}: Inválido")
			except OSError as err:
				print(err)
		else: #Pegando CPF da linha de comando
			if cpft.verifica_cpf(args.name):
				print("Válido")
			else:
				print("Inválido")
	elif args.command == 'gen':
		for i in range(args.n):
			print(cpft.gerar_cpf())
	else:
		parser.exit("cpftools [OPTIONS] [ARGUMENTS]\ncpftools --help para mais informações");


if __name__ == "__main__":
    main()