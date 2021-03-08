class Custo:
  def __init__(self, data, descricao, valor):
    self._data = data
    self._descricao = descricao
    self._valor = valor

  # Gets
  @property
  def data(self):
    return str(self._data)

  @property
  def descricao(self):
    return str(self._descricao)

  @property
  def valor(self):
    return float(self._valor)

  # Sets
  @data.setter
  def data(self, nova_data):
    self._data = nova_data

  @descricao.setter
  def descricao(self, nova_descricao):
    self._descricao = nova_descricao

  @valor.setter
  def valor(self, novo_valor):
    self._valor = novo_valor

  def __str__(self):
    return f'Custo:\n  Data:{self._data}\n  Descrição{self._descricao}\n  Valor: {self._valor}'
