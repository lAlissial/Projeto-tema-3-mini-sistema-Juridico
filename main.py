from advogado import *
from audiencia import *
from pessoa import *
from custo import *
from processo import *
from frufru import *

# ----------------------------------------------------------------- OBJETOS -----------------------------------------------------------------
custo1 = Custo('14/10/2020', 'Ação de Alimentos Gravídicos', 1500)
custo2 = Custo('11/05/2019', 'Ação de Divórcio Litigioso', 5000)
custo3 = Custo('27/03/2021', 'Ação de Guarda Compartilhada', 2500)
custo4 = Custo('30/01/2021', 'Ação Indenizatória por Danos Morais', 2000)


lista_pro_adv_1 = []
lista_pro_adv_2 = []
lista_pro_adv_3 = []
lista_de_processos1 = []
lista_de_audiencias1 = []
lista_de_audiencias2 = []
lista_de_audiencias3 = []
lista_de_audiencias4 = []
lista_de_audiencias5 = []
lista_de_processos2 = []
lista_de_processos3 = []
lista_de_processos4 = []


advogado1 = Advogado('7850', 'Marcos Inácio', lista_pro_adv_1)
advogado2 = Advogado('21840', 'João José', lista_pro_adv_2)
advogado3 = Advogado('15245', 'Samara Dantas da Silva', lista_pro_adv_3)
# se for criar um advogado lembrar de: adicionar ele na 'lista_de_todos_advogados', criar uma 'lista_pro_adv_numero' p ele
# e nessa lista tbm adicionar os processos q o advogado está representando

pessoa1 = Pessoa('156.856.943-52', 'André Coelho de Sá', lista_de_processos1)
pessoa2 = Pessoa("425.652.214-20", "Sabrina Sebastiana", lista_de_processos2)
pessoa3 = Pessoa("251.235.201-52", "Soraya Pitanga Bezerra", lista_de_processos3)
pessoa4 = Pessoa("298.915.101-72", "Ana Maia de Souza", lista_de_processos4)
# se for criar uma pessoa nova lembrar de: adicionar ela na 'lista_de_todas_pessoas', criar uma lista de processos pra ela 
# e vai ter q add processos nessas listas  

pro1 = Processo('Processo de relacionado a Ação de Alimentos Gravídicos', custo1, True, 'Em trâmite', pessoa1, advogado1, lista_de_audiencias1)
pro2 = Processo('Processo relacionado a Ação de Divórcio Litigioso', custo2, False, 'Em trâmite', pessoa4, advogado3, lista_de_audiencias2)
# se for criar um novo processo lembrar de: adicionar ele na lista 'lista_de_todos_processos', criar uma lista de audiencias p ele


lista_de_processos1.append(pro1)
lista_de_processos4.append(pro2)



lista_pro_adv_1.append(pro1)
lista_pro_adv_3.append(pro2)


pro3 = Processo('Processo relacionado a Ação de Guarda Compartilhada', custo3, True, 'Em trâmite', pessoa1, advogado1, lista_de_audiencias3)
pro4 = Processo('Processo relacionado a Ação Indenizatória por Danos Morais', custo4, False, 'Finalizado', pessoa2, advogado2, lista_de_audiencias4)

lista_de_processos1.append(pro3)
lista_de_processos2.append(pro4)

lista_pro_adv_1.append(pro3)
lista_pro_adv_2.append(pro4)


pro5 = Processo('Processo relacionado a Ação de Divórcio Litigioso', custo2, True, 'Em trâmite', pessoa3, advogado2, lista_de_audiencias5)

lista_de_processos3.append(pro5)

lista_pro_adv_2.append(pro5)


a1 = Audiencia('08/09/2019', 'Audiência de Mediação', 90)
a2 = Audiencia('07/10/2019', 'Audiência de Justificação Prévia', 120)
a3 = Audiencia('05/12/2021', 'Audiência de Instrução e Julgamento', 70)
lista_de_audiencias1.append(a1)
lista_de_audiencias1.append(a2)
lista_de_audiencias1.append(a3)

a4 = Audiencia('15/10/2020', 'Audiência Preliminar', 40)
a5 = Audiencia('12/05/2019', 'Tutela de Urgência', 30)
a6 = Audiencia('28/03/2021', 'Audiência de Justificação de Tutela', 25)
lista_de_audiencias2.append(a4)
lista_de_audiencias2.append(a5)
lista_de_audiencias2.append(a6)

a7 = Audiencia('15/10/2018', 'Audiência de Conciliação', 50)
a8 = Audiencia('12/05/2017', 'Audiência de Justificação de Tutela Antecipada', 70)
a9 = Audiencia('28/03/2029', 'Audiência de Instrução e Julgamento', 65)
lista_de_audiencias3.append(a7)
lista_de_audiencias3.append(a8)
lista_de_audiencias3.append(a9)

a10 = Audiencia('06/06/2021', 'Audiência de Mediação', 30)
a11 = Audiencia('19/05/2020', 'Audiência de Instrução e Julgamento', 80)
lista_de_audiencias4.append(a10)
lista_de_audiencias4.append(a11)

a12 = Audiencia('11/03/2021', 'Audiência de Mediação', 20)
a13 = Audiencia('13/01/2019', 'Audiência de Instrução e Julgamento', 90)
lista_de_audiencias5.append(a12)
lista_de_audiencias5.append(a13)



lista_de_todos_processos = []
lista_de_todos_processos.append(pro1)
lista_de_todos_processos.append(pro2)
lista_de_todos_processos.append(pro3)
lista_de_todos_processos.append(pro4)
lista_de_todos_processos.append(pro5)


lista_de_todas_pessoas = []
lista_de_todas_pessoas.append(pessoa1)
lista_de_todas_pessoas.append(pessoa2)
lista_de_todas_pessoas.append(pessoa3)
lista_de_todas_pessoas.append(pessoa4)

lista_de_todos_advogados = []
lista_de_todos_advogados.append(advogado1)
lista_de_todos_advogados.append(advogado2)
lista_de_todos_advogados.append(advogado3)

#---------------------------------------------------------------------------------------------------------------------------------------------






print(f'*' * 50)
print(f"{c[10]}{'MINI-SISTEMA JURÍDICO':^50}{c[0]}")
print(f'*' * 50)

while True:
    resp = menu(["Buscar Audiências (por duração)", "Decisões Processuais", "Custos Processuais (Cliente/Advogado)", "Clientes por advogado", "Audiências que já ocorreram", "Filtrar audiencias de processo por uma palavra", "Sair do Sistema"],"MENU PRINCIPAL")
    if resp == 1:
        for j in range(len(lista_de_todos_processos)):
            print(f'  Processo[{j}]: {lista_de_todos_processos[j]}')
            print(f'    Decisão: {lista_de_todos_processos[j].decisoes()}\n')
        try:
            qual_processo = int(input("Você gostaria de buscar pelas audiências de qual processo ?[apenas o número] "))
            qual_tempo = int(input('Digite o tempo em minutos da audiência a ser buscada: '))
            print((f'\n{c[2]}Audiências com tempo maior ou igual ao informado:{c[0]}\n'))
            print(lista_de_todos_processos[qual_processo].audiencias_temp(qual_tempo))
        except IndexError:
            print(f'{c[30]}Não encontradas! Informe um número de processo válido!{c[0]}')
        except ValueError:
            print(f'{c[30]}Não encontradas! Informe um valor válido!{c[0]}')


    if resp == 2:
        for i in range(len(lista_de_todas_pessoas)):
            print(f'\nPessoa[{i}]:')
            print(f'  Nome: {lista_de_todas_pessoas[i].nome}\n  CPF: {lista_de_todas_pessoas[i].cpf}\n')
        try:
            qual_pessoa = int(input('Digite o número da pessoa da qual deseja acessar os processos e suas respectivas decisões: '))
            qual_decisao = menu(['Deferidos', 'Inderidos'],'Deseja ver a quantidade de processos:')
            if qual_decisao == 1:
                print(f'{lista_de_todas_pessoas[qual_pessoa].num_decisoes(True)}') # Lembrar que ele so contabiliza os que estão 'em trâmite', o finalizado ele n leva em conta
            if qual_decisao == 2:
                print(f'{lista_de_todas_pessoas[qual_pessoa].num_decisoes(False)}')
        except IndexError:
            print(f'{c[30]}Número de pessoa inválido!{c[0]}')
        except ValueError:
            print(f'{c[30]}Valor inválido!{c[0]}')


    if resp == 3:
        pessoa_ou_advogado = menu(['Pessoa','Advogado'],'Gostaria de acessar os custos dos processos de:')
        if pessoa_ou_advogado == 1:
            for i in range(len(lista_de_todas_pessoas)):
                print(f'\nPessoa[{i}]:')
                print(f'  Nome: {lista_de_todas_pessoas[i].nome}\n  CPF: {lista_de_todas_pessoas[i].cpf}\n')
            try:
                qual_a_pessoa = int(input('Digite o número da pessoa da qual desejar acessar os custos de seus processos: '))
                print(f'{lista_de_todas_pessoas[qual_a_pessoa].custo_total()}')
            except:
                print(f'{c[30]}Número inválido!{c[0]}')
        if pessoa_ou_advogado == 2:
            for i in range(len(lista_de_todos_advogados)):
                print(f'\nAdvogado[{i}]:')
                print(f'Nome: {lista_de_todos_advogados[i].nome}\nCódigo OAB: {lista_de_todos_advogados[i].cod_oab}\n')
            try:
                qual_o_advogado = int(input('Digite o número do advogado da qual desejar acessar os custos de seus processos: '))
                qual_o_cod = str(input('Informe o código OAB do advogado em questão: ')).strip()
                print(f'{lista_de_todas_pessoas[qual_o_advogado].custo_total_adv(qual_o_cod)}')
            except IndexError:
                print(f'{c[30]}Número do advogado inválido!{c[0]}')
            except ValueError:
                print(f'{c[30]}Valor inválido!{c[0]}')
        if pessoa_ou_advogado != 1 and pessoa_ou_advogado != 2:
            print(f'{c[17]}Opção inválida!{c[0]}')


    if resp == 4:
        for i in range(len(lista_de_todos_advogados)):
            print(f'\nAdvogado[{i}]:')
            print(f'Nome: {lista_de_todos_advogados[i].nome}')
        try:
            lista_de_qual_advogado = int(input('\nVocê gostaria de saber a lista de cliente de qual advogado? '))
            print(linha())
            print(f'{c[15]}{"NOME DE TODOS OS CLIENTES DESSE ADVOGADO":^50}{c[0]}')
            print(linha())
            for i in range(len(lista_de_todos_advogados[lista_de_qual_advogado].lista_clientes())):
                print(lista_de_todos_advogados[lista_de_qual_advogado].lista_clientes()[i])# p mostrar 1 cliente por vez
        except:
            print(f'{c[30]}Não encontrados visto que foi informado um valor inválido de advogado!{c[0]}')


    if resp == 5:
        for i in range(len(lista_de_todos_processos)):
            print(f'\n  Processo[{i}]: {lista_de_todos_processos[i]}')
        try:
            qual_processo_para_audiencia = int(input("\nDe qual processo você gostaria de buscar as audiências que já passaram??[apenas o número] "))
            print(linha())
            print(f'{c[11]}{"AUDIÊNCIAS QUE JÁ OCORRERAM":^50}{c[0]}')
            print(linha())
            print(lista_de_todos_processos[qual_processo_para_audiencia].audiencias_que_ja_ocorreram())
        except:
            print(f'{c[30]}Não encontradas pois foi digitado um valor de processo inválido !{c[0]}')


    if resp == 6:
        for j in range(len(lista_de_todos_processos)):
            print(f'\n  Processo[{j}]: {lista_de_todos_processos[j]}')
        try:
            qual_processo_para_filtrar = int(input("\nDe qual processo você gostaria de buscar as audiências para fazer a filtragem? "))
            qual_palavra = str(input('Por qual palavra deseja filtrar? '))
            print(linha())
            print(f'{c[3]}{"AUDIÊNCIAS FILTRADAS":^50}{c[0]}')
            print(linha())
            print(lista_de_todos_processos[qual_processo_para_filtrar].filtrar_audiencia_do_processo(qual_palavra))
        except:
            print(f'{c[30]}Nenhuma dado que um valor inválido de processo foi digitado!{c[0]}')

    if resp == 7:
        cabecalho('ATÉ LOGO!')
        break
