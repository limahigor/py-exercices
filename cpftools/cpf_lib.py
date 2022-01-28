from random import randint
from random import choice

def cpf_format(cpf):
  string_cpf = "".join(map(str, cpf))

  string_cpf = string_cpf[0:3] + "." + string_cpf[3:6] + "." + string_cpf[6:9] + "-" + string_cpf[9:12]

  return string_cpf

def segundo_digito(cpf):
  multi = []
  for i, j in zip(cpf, range(11, 1, -1)): #Itera o cpf com uma lista de 11 à 2 e multiplica os respectivos valores
    multi.append(i*j) #Salva o resultado na list
  soma = sum(multi)
  digito = 11 - soma%11

  if digito >= 10:
    return 0
  return digito

def primeiro_digito(cpf):
  multi = []
  for i, j in zip(cpf, range(10, 1, -1)): #Itera o cpf com uma lista de 10 à 2 e multiplica os respectivos valores
    multi.append(i*j) #Salva o resultado na lista
  soma = sum(multi)
  digito = 11 - soma%11

  if digito >= 10:
    return 0
  return digito

def verifica_cpf(cpf):
  cpf = ''.join(filter(str.isdigit, cpf)) #Remove os '.' e '-' e pega apenas os numeros
  cpf = list(map(int, cpf)) #Transforma os caracteres em numeros e transforma em uma lista
  if len(cpf) != 11:
    return 0
  else:
    if(primeiro_digito(cpf) == cpf[9]):
      if segundo_digito(cpf) == cpf[10]:
        return 1
      else:
        return 0
    else:
      return 0

def gerar_cpf():
  cpf = []
  seq = []

  while len(cpf) < 9:
    for i in range(1, 101):
      seq.append(randint(0, 9))
    cpf.append(choice(seq))

  cpf.append(primeiro_digito(cpf))
  cpf.append(segundo_digito(cpf))

  cpf = cpf_format(cpf)
  return cpf