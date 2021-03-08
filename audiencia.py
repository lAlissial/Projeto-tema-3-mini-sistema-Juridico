class Audiencia:
    def __init__(self, data, recomendacao, duracao):
        self._data = data
        self._recomendacao = recomendacao
        self._duracao = duracao

    # Gets
    @property
    def data(self):
        return str(self._data)

    @property
    def recomendacao(self):
        return str(self._recomendacao)

    @property
    def duracao(self):
        return int(self._duracao)

    # Sets
    @data.setter
    def data(self, nova_data):
        self._data = nova_data

    @recomendacao.setter
    def recomendacao(self, nova_recomendacao):
        self._recomendacao = nova_recomendacao

    @duracao.setter
    def duracao(self, nova_duracao):
        self._duracao = nova_duracao

    def __str__(self):
        return f'Audiência:\n  Data{self._data}\n  Recomendação{self._recomendacao}\n  Duração: {self._duracao} minutos'
