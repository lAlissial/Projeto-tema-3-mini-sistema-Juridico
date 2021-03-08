class Advogado:
  def __init__(self, cod_oab, nome, processos=[]):
    self._cod_oab = cod_oab
    self._nome = nome
    self._processos = processos

  # Gets
  @property
  def cod_oab(self):
    return str(self._cod_oab)

  @property
  def nome(self):
    return str(self._nome)

  @property
  def processos(self):
    return self._processos

  # Sets
  @cod_oab.setter
  def cod_oab(self, novo_cod_oab):
    self._cod_oab = novo_cod_oab

  @nome.setter
  def nome(self, novo_nome):
    self._nome = novo_nome

  @processos.setter
  def processos(self, novo_processos):
    self._processos.append(novo_processos)

  # Métodos
  def lista_clientes(self):
    lista_de_clientes_do_advogado = []
    for i in range(len(self._processos)):
      if self._processos[i].pessoa.nome not in lista_de_clientes_do_advogado:
        lista_de_clientes_do_advogado.append(self._processos[i].pessoa.nome)
    return lista_de_clientes_do_advogado


  def __str__(self):
    output_do_advogado = ''
    output_do_advogado += (f'COD-OAB:{self._cod_oab}\nNome: {self._nome}')
    for i in range(len(self._processos)):
      output_do_advogado += (f'\nProcesso[{i}]')
      output_do_advogado += (f'\nDescrição:{self._processos[i].descricao}\nPessoa-> {self._processos[i].pessoa}\n')
    return output_do_advogado