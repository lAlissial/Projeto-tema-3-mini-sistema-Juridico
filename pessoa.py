class Pessoa:
  def __init__(self, cpf, nome, processos=[]):
    self._cpf = cpf
    self._nome = nome
    self._processos = processos

  # Gets
  @property
  def cpf(self):
    return str(self._cpf)

  @property
  def nome(self):
    return str(self._nome)

  @property
  def processos(self):
    return self._processos

  # Sets
  @cpf.setter
  def cpf(self, novo_cpf):
    self._cpf = novo_cpf

  @nome.setter
  def nome(self, novo_nome):
    self._nome = novo_nome

  @processos.setter
  def processos(self, novo_processo):
    self._processos.append(novo_processo)

  # Métodos
  def num_decisoes(self, dec):
    contador_deferido = 0
    contador_indeferido = 0
    resultado_num_decisoes = 0
    for i in range(len(self._processos)):
      if self._processos[i].status == 'Em trâmite':
        if dec is True and self._processos[i].decisao == dec:
          contador_deferido += 1
        if dec is False and self._processos[i].decisao == dec:
          contador_indeferido += 1
      if dec is True:
        resultado_num_decisoes = f'A quantidade de processos deferidos é: {contador_deferido}'
      else:
        resultado_num_decisoes = f'A quantidade de processos indeferidos é: {contador_indeferido}'
    return resultado_num_decisoes

  def custo_total(self):
    custo_de_todos_processos = 0
    for i in range(len(self._processos)):
      custo_de_todos_processos += self._processos[i].custo.valor
    return f'O custo total de seus processos é: R${custo_de_todos_processos}'


  def custo_total_adv(self, cod_oab):
    custo_de_todos_processos_advogado = 0
    for i in range(len(self._processos)):
      if self._processos[i].advogado.cod_oab == cod_oab:
        custo_de_todos_processos_advogado += self._processos[i].custo.valor
    return f'O valor dos processos representados pelo advogado de código [{cod_oab}]: R${custo_de_todos_processos_advogado}'

  def __str__(self):
    output_de_pessoa = ''
    output_de_pessoa += (f'CPF: {self._cpf}, Nome:{self._nome}, Processos:')
    for i in range(len(self._processos)):
      output_de_pessoa += (f' {self._processos[i].descricao},')
    return output_de_pessoa

