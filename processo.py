from datetime import date

class Processo:
    def __init__(self, descricao, custo, decisao, status, pessoa, advogado, audiencias=[]):
        self._descricao = descricao
        self._custo = custo
        self._decisao = decisao
        self._status = status
        self._pessoa = pessoa
        self._advogado = advogado
        self._audiencias = audiencias

    # Gets
    @property
    def descricao(self):
        return str(self._descricao)

    @property
    def custo(self):
        return self._custo

    @property
    def decisao(self):
        return bool(self._decisao)

    @property
    def status(self):
        return str(self._status)

    @property
    def pessoa(self):
        return self._pessoa

    @property
    def advogado(self):
        return self._advogado

    @property
    def audiencias(self):
        return self._audiencias

    # Sets
    @descricao.setter
    def descricao(self, nova_descricao):
        self._descricao = nova_descricao

    @custo.setter
    def custo(self, novo_custo):
        self._custo = novo_custo

    @decisao.setter
    def decisao(self, nova_decisao):
        self._decisao = nova_decisao

    @status.setter
    def status(self, novo_status):
        self._status = novo_status

    @pessoa.setter
    def pessoa(self, nova_pessoa):
        self._pessoa = nova_pessoa

    @advogado.setter
    def advogado(self, novo_advogado):
        self._advogado = novo_advogado

    @audiencias.setter
    def audiencias(self, novas_audiencias):
        self._audiencias.append(novas_audiencias)

    # Métodos
    def audiencias_temp(self, tempo):
        output_audiencias_temp = ''
        for i in range(len(self._audiencias)):
            if self._audiencias[i].duracao >= tempo:
                output_audiencias_temp += (f'\nData: {self._audiencias[i].data}\nRecomendação: {self._audiencias[i].recomendacao}\nDuração: {self._audiencias[i].duracao}\n')
            else:
                if output_audiencias_temp == '' and 'Nenhuma audiência encontrada com o tempo maior ou igual ao informado' not in output_audiencias_temp:
                    output_audiencias_temp += (f'Nenhuma audiência encontrada com o tempo maior ou igual ao informado')
        return output_audiencias_temp


    def decisoes(self):
        if self.decisao is True:
            return "Deferido"
        else:
            return "Indeferido"

    def audiencias_que_ja_ocorreram(self):
        data_atual = date.today()
        output_audiencias_que_ja_ocorreram = ''
        for i in range(len(self._audiencias)):
            dia_tal = self._audiencias[i].data[:2]
            mes_tal = self._audiencias[i].data[3:5]
            ano_tal = self._audiencias[i].data[6:]
            data_audiencia = date(int(ano_tal), int(mes_tal), int(dia_tal))
            if data_atual > data_audiencia:
                output_audiencias_que_ja_ocorreram += (f'\nData: {self._audiencias[i].data}\nRecomendação: {self._audiencias[i].recomendacao}\n')
        return output_audiencias_que_ja_ocorreram

    def filtrar_audiencia_do_processo(self, palavra):
        output_filtrar_audiencia_do_processo = ''
        for i in range(len(self._audiencias)):
            if palavra.lower() in self._audiencias[i].recomendacao.lower():
                output_filtrar_audiencia_do_processo += (f'\n  Data: {self._audiencias[i].data}\n  Recomendação: {self._audiencias[i].recomendacao}\n  Duração: {self._audiencias[i].duracao} minutos\n')
            else:
                if output_filtrar_audiencia_do_processo == '' and 'Nenhuma audiência encontrada com essa palavra' not in output_filtrar_audiencia_do_processo:
                    output_filtrar_audiencia_do_processo += (f'Nenhuma audiência encontrada com essa palavra')
        return output_filtrar_audiencia_do_processo


    def __str__(self):
        return f'{self._descricao} ' \
               f'\n    Valor da Causa: R${self._custo.valor}' \
               f'\n    Situação: {self._status}' \
               f'\n    Decisão: {self.decisoes()}' \
               f'\n    Parte interessada: {self._pessoa.nome}' \
               f'\n    Advogado: {self._advogado.nome}'
