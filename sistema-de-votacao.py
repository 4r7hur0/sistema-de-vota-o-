''''/*******************************************************************************
Autor: Carlos Arthur Batista Nunes
Componente Curricular: MI de Algoritimos
Concluido em: 16/06/2023
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
******************************************************************************************/'''
candidatos = []
votantesL = []
votantesC = {'Servidor Doscente': 0, 'Servidor Técnico': 0, 'Discente': 0}
urnas = {'u1': [], 'u2': [], 'u3': [], 'u4': []}
dias = {1: [], 2: [], 3: []}
votos_nulos = {'Servidor Doscente': {1: 0, 2: 0, 3: 0}, 'Servidor Técnico': {1: 0, 2: 0, 3: 0}, 'Discente': {1: 0, 2: 0, 3: 0}}
votos_brancos = {'Servidor Doscente': {1: 0, 2: 0, 3: 0}, 'Servidor Técnico': {1: 0, 2: 0, 3: 0}, 'Discente': {1: 0, 2: 0, 3: 0}}
categorias = {'Servidor Doscente': {1: 0, 2: 0, 3: 0}, 'Servidor Técnico': {1: 0, 2: 0, 3: 0}, 'Discente': {1: 0, 2: 0, 3: 0}}
total_urna = {'urna1': 0, 'urna2': 0, 'urna3': 0, 'urna4': 0}
num_chapasD = {}
num_chapasT = {}
num_chapasDI = {}
# classe para cadastrar os candidatos
class Candidato:
    def __init__(self, reitor, vice_reitor, nome_chapa):
        self.reitor = reitor
        self.vice_reitor = vice_reitor
        self.nome_chapa = nome_chapa

    # Função para salvar as chapas em arquivo
    def salvar_chapa(candidatos):
        with open('chapas.txt', 'w') as arquivo:
            for chapa in candidatos:
                arquivo.write(f'Nome da chapa: {chapa.nome_chapa}\n')
                arquivo.write(f'Reitor: {chapa.reitor}\n')
                arquivo.write(f'Vice-Reitor: {chapa.vice_reitor}\n')
                arquivo.write(f'----------------------------------------\n')
                print('Chapas salvas com sucesso.\n')

    # Função para cadastrar uma chapa
    def cadastramento():
        nome_chapa = input('Qual o nome da chapa.\n').upper()
        reitor = input('Digite o nome do candidato para reitor.\n')
        vice_reitor = input('Digite o nome do candidato para vice-reitor\n')
        chapa = Candidato(reitor, vice_reitor, nome_chapa)
        return chapa

    # Função para modificar a chapa
    def modificar_chapa(candidatos):
        nome_chapa = input('Digite o nome da chapa que deseja modificar.\n')
        # procuarar a chapa na lista de candidatos
        for chap in candidatos:
            if chap.nome_chapa == nome_chapa:
                print('Chapa encontrada!')
                print('Quem deseja modificar:')
                print('1. Reitor')
                print('2. Vice-reitor')
                while True:
                    try:
                        escolha = int(input('Digite a opção desejada\n'))
                        if 1 > escolha > 2:
                            print('Digite um número entre 1 e 2')
                            continue
                        else:
                            break
                    except:
                        print('Digite somente números entre 1 e 2')
                        continue
                if escolha == 1:
                    novo_nome = input('Digite o novo nome.\n')
                    chap.reitor = novo_nome
                    return
                else:
                    novo_nome = input('Digite o novo nome.\n')
                    chap.vice_reitor = novo_nome
                    return
            print('Chapa não encontrada!')

    # Função para excluir uma chapa
    def excluir_chapa(candidatos):
        nome_chapa = input('Qual o nome da chapa que deseja excluir.\n').upper()
        # Procurar pelo nome da chapa
        for chapa in candidatos:
            if chapa.nome_chapa == nome_chapa:
                print('Chapa encontrada')
                candidatos.remove(chapa)
                print('Chapa exclída com sucesso.')

    # Função para mostrar as chapas
    def mostrar_chapa(candidatos):
        print('''     >>>>> Candidatos cadastrados <<<<<''')
        if candidatos == []:
            print('Nenhuma chapa foi cadastrada.\n')
        else:
            for chapas in candidatos:
                print(f'Chapa: {chapas.nome_chapa}')
                print(f'Candidato para reitor: {chapas.reitor}')
                print(f'Candidato para vice-reitor: {chapas.vice_reitor}')

class Votante:
    def __init__(self, nome, categoria, voto, urna, dia):
        self.nome = nome
        self.categoria = categoria
        self.voto = voto
        self.urna = urna
        self.dia = dia

    def votar(votantes, urna, dia, total_urna, ntsd, ntst, ntd):
        while True:
            nome = input('Qual o seu nome?\n').upper()
            primeira_letra = nome[0]
            if primeira_letra == 'A' or primeira_letra == 'B' or primeira_letra == 'C' or primeira_letra == 'D':
                print('Seu módlulo de votação é o 1.')
                urna = 'u1'
                total_urna["urna1"] += 1
                break
            elif primeira_letra == 'E' or primeira_letra == 'F' or primeira_letra == 'G' or primeira_letra == 'H' or primeira_letra == 'I' or primeira_letra == 'J':
                print('Seu módulo de votação é o 3')
                urna = 'u2'
                total_urna["urna2"] += 1
                break
            elif primeira_letra == 'K' or primeira_letra == 'L' or primeira_letra == 'M' or primeira_letra == 'N' or primeira_letra == 'O':
                print('Seu módulo de votação é o 5')
                urna = 'u3'
                total_urna["urna3"] += 1
                break
            elif primeira_letra == 'P' or primeira_letra == 'Q' or primeira_letra == 'R' or primeira_letra == 'S' or primeira_letra == 'T' or primeira_letra == 'U' or primeira_letra == 'V' or primeira_letra == 'W' or primeira_letra == 'X' or primeira_letra == 'Y' or primeira_letra == 'Z':
                print('Seu módulo de votação é o 7')
                urna = 'u4'
                total_urna["urna4"] += 1
                break
            else:
                print('Digite um nome válido.')
                continue
        print('Digite sua categoria:')
        print('1. Servidor Técnico-administrativo')
        print('2. Servidor Docente')
        print('3. Discente')
        while True:
            try:
                categoria = int(input('Digite a opção desejada\n'))
                if 1 > categoria > 3:
                    print('Digite um número entre 1 e 3')
                    continue
                else:
                    if categoria == 1:
                        categoria = 'Servidor Técnico'
                        if ntst == 0:
                            print('Todos da categoria já votaram.')
                            continue
                        else:
                            ntst -= 1
                            if dia == 1:
                                categorias[categoria][dia] += 1
                                votantesC[categoria] += 1
                            elif dia == 2:
                                categorias[categoria][dia] += 1
                                votantesC[categoria] += 1
                            elif dia == 3:
                                categorias[categoria][dia] += 1
                                votantesC[categoria] += 1
                        break
                    if categoria == 2:
                        categoria = 'Servidor Doscente'
                        if ntsd == 0:
                            print('Todos da categoria já votaram.')
                            continue
                        else:
                            ntsd -= 1
                            if dia == 1:
                                categorias[categoria][dia] += 1
                                votantesC[categoria] += 1
                            elif dia == 2:
                                categorias[categoria][dia] += 1
                                votantesC[categoria] += 1
                            elif dia == 3:
                                categorias[categoria][dia] += 1
                                votantesC[categoria] += 1
                        break
                    if categoria == 3:
                        categoria = 'Discente'
                        if ntd == 0:
                            print('Todos da categoria já votaram.')
                            continue
                        else:
                            ntd -= 1
                            if dia == 1:
                                categorias[categoria][dia] += 1
                                votantesC[categoria] += 1
                            elif dia == 2:
                                categorias[categoria][dia] += 1
                                votantesC[categoria] += 1
                            elif dia == 3:
                                categorias[categoria][dia] += 1
                                votantesC[categoria] += 1
                        break
            except:
                print('Digite somente números entre 1 e 3')
                continue
        print('Escolha em qual chapa irá votar:')
        for chapa in candidatos:
            print(f'nome da chapa: {chapa.nome_chapa}')
            print(f'Candidato para Reitor: {chapa.reitor}')
            print(f'Candidato para Vice-Reitor: {chapa.vice_reitor}')
            print('------------------------------------------------')
        print('Nulo/Branco')
        while True:
            voto_sucesso = False
            voto = input('Digite o nome da chapa ou se deseja votar branco/nulo.\n').upper()
            if voto == 'NULO' or voto == 'BRANCO':
                print('Voto cadastrado com sucesso.')
                break
            for chapa in candidatos:
                if chapa.nome_chapa == voto:
                    print('Voto cadastrado com sucesso.')
                    voto_sucesso = True
            if voto_sucesso == True:
                break
            else:
                print('Digite uma chapa válida.')
                continue
        votante = Votante(nome, categoria, voto, urna, dia)
        votantesL.append(votante)
        return votante, ntsd, ntst, ntd

def salvar_dados(urnas, dia, total):
    with open(f'dados dia {dia}.txt', 'w') as arquivo:
        diaa = 1
        arquivo.write(f'Dia {dia}:\n')
        for di, votante in urnas.items():
            arquivo.write(f'Foram {len(votante)} eleitores na {di}\n')
            for votantes in votante:
                arquivo.write(f'Nome: {votantes.nome}\n')
                arquivo.write(f'Categoria: {votantes.categoria}\n')
                arquivo.write(f'Voto na chapa: {votantes.voto}\n')
        arquivo.write(f'Número de ausentes no dia {dia}: {total}')
        arquivo.write('\n')
        diaa += 1

def votos_nulo_branco(votantesL):
    for voto in votantesL:
        if voto.voto == 'NULO':
            votos_nulos[voto.categoria][voto.dia] += 1
        elif voto.voto == 'BRANCO':
            votos_nulos[voto.categoria][voto.dia] += 1

def criar_dic(candidatos, d, t, di,votantesL):
    for i in candidatos:
        d[i.nome_chapa] = 0
        t[i.nome_chapa] = 0
        di[i.nome_chapa] = 0
    for i in candidatos:
        for j in votantesL:
            if j.categoria == 'Servidor Doscente':
                if j.voto == i.nome_chapa:
                    d[i.nome_chapa] += 1
            elif j.categoria == 'Servidor Técnico':
                if j.voto == i.nome_chapa:
                    t[i.nome_chapa] += 1
            elif j.categoria == 'Discente':
                if j.voto == i.nome_chapa:
                    num_chapasDI[i.nome_chapa] += 1


#main():
while True:
    try:
        NTSD = int(input('Digite o Número total de servidores docentes votantes.\n'))
        NTST = int(input('Digite o Número total de servidores técnicos votantes.\n'))
        NTD = int(input('Digite o Número total de discentes votantes.\n'))
        break
    except:
        print('Digite somente números')
ntsd = NTSD
ntst = NTST
ntd = NTD
total_eleitores = NTSD + NTST + NTD

while True:
    # Menu de cadastramento
    print('''     >>>>> Menu <<<<<''')
    print('1. Cadastrar uma chapa')
    print('2. Listar as chapas')
    print('3. Modificar uma chapa')
    print('4. Excluir uma chapa')
    print('5. Sair')
    while True:
        try:
            escolha = int(input('Digite a opção desejada:\n'))
            if escolha < 1 or escolha > 5:
                print('Digite um número entre 1 e 5')
            else:
                break
        except ValueError:
            print('Digite somente números')
    if escolha == 1:
        chapa = Candidato.cadastramento()
        candidatos.append(chapa)
        print('Chapa cadastrada.')

    elif escolha == 2:
        Candidato.mostrar_chapa(candidatos)

    elif escolha == 3:
        Candidato.modificar_chapa(candidatos)

    elif escolha == 4:
        Candidato.excluir_chapa(candidatos)

    elif escolha == 5:
        print('Cadastramento encerrado.')
        Candidato.salvar_chapa(candidatos)
        break

#Segunda parte (votação)
dia = 1
voto_1 = voto_2 = voto_3 = 0
while True:
    if dia > 3:
        print('Votação encerrada. Os dados serão salvos.')

        break
    print(f'Inicio da votação dia {dia}')
    escolha = input(f'Exite algum eleitor para o dia {dia}?(S = Sim / N =Não)\n').upper()
    if escolha == 'S':
        if dia == 1:
            votante, ntsd, ntst, ntd = Votante.votar(votantesC, urnas, dia, total_urna, ntsd, ntst, ntd)
            voto_1 += 1
            if votante.urna == 'u1':
                urnas["u1"].append(votante)
            elif votante.urna == 'u2':
                urnas["u2"].append(votante)
            elif votante.urna == 'u3':
                urnas["u3"].append(votante)
            elif votante.urna == 'u4':
                urnas["u4"].append(votante)
            total_eleitores -= 1
        elif dia == 2:
            votante, ntsd, ntst, ntd = Votante.votar(votantesC, urnas, dia, total_urna, ntsd, ntst, ntd)
            voto_2 += 1
            if votante.urna == 'u1':
                urnas["u1"].append(votante)
            elif votante.urna == 'u2':
                urnas["u2"].append(votante)
            elif votante.urna == 'u3':
                urnas["u3"].append(votante)
            elif votante.urna == 'u4':
                urnas["u4"].append(votante)
            total_eleitores -= 1
        elif dia == 3:
            votante, ntsd, ntst, ntd = Votante.votar(votantesC, urnas, dia, total_urna, ntsd, ntst, ntd)
            voto_3 += 1
            if votante.urna == 'u1':
                urnas["u1"].append(votante)
            elif votante.urna == 'u2':
                urnas["u2"].append(votante)
            elif votante.urna == 'u3':
                urnas["u3"].append(votante)
            elif votante.urna == 'u4':
                urnas["u4"].append(votante)
            total_eleitores -= 1
    elif escolha == 'N':
        print('O dia será avançado. Os dados serão salvos.')
        salvar_dados(urnas, dia, total_eleitores)
        dia += 1
        continue
    else:
        print('Digite somente S (para sim) e N (para não)')
    while True:
        escolha = input('Mais algum votante para este dia?(S = Sim / N = Não)\n').upper()
        if escolha == 'S' or escolha == 'N':
            break
        else:
            print('Digite um valor válido para a escolha')
            continue
    if escolha == 'N':
        print('O dia será avançado.')
        salvar_dados(urnas, dia, total_eleitores)
        urnas = {'u1': [], 'u2': [], 'u3': [], 'u4': []}
        dia += 1

# Saída dos dados
total_nulo = total_branco = 0
criar_dic(candidatos, num_chapasD, num_chapasT, num_chapasDI, votantesL)
print(num_chapasD, num_chapasT, num_chapasDI)
while True:
    # Menu de saída de dados
    print('''     >>>>> Menu <<<<<''')
    print('1. Número de votantes por dia/categoria')
    print('2. Número de votos Nulo/Branco por dia/categoria')
    print('3. Número total de votos Nulo/Branco')
    print('4. Total de votos computados em cada urna')
    print('5. NVSD = Número de votos em cada chapa dos servidores docentes')
    print('6. NVST = Número de votos em cada chapa dos servidores técnicos')
    print('7. NVD = Número de votos em cada chapa dos discentes')
    print('8. Porcentagem de ausência por categoria')
    print('9. Escore de cada chapa')
    print('10. Finalizar Programa')
    while True:
        try:
            escolha = int(input('Digite a opção desejada\n'))
            if 1 > escolha > 10:
                print('Digite um número entre 1 e 10')
                continue
            else:
                break
        except:
            print('Digite somente números entre 1 e 10')
            continue
    if escolha == 1:
        print(f'O número de votos no dia 1 foi {voto_1}')
        print(f'O número de votos no dia 2 foi {voto_2}')
        print(f'O número de votos no dia 3 foi {voto_3}')
        for k, v in categorias.items():
            for g, h in v.items():
                print(f'A categoria {k} teve {h} votos no dia {g}')

    elif escolha == 2:
        votos_nulo_branco(votantesL)
        print('>>>>>VOTOS NULOS<<<<< ')
        for k, v in votos_nulos.items():
            for g, h in v.items():
                print(f'No dia {g} tiveram {h} votos nulos da categoria {k}')
                total_nulo += h
        print('>>>>>VOTOS BRANCOS<<<<<')
        for k, v in votos_brancos.items():
            for g, h in v.items():
                print(f'No dia {g} tiveram {h} votos brancos da categoria {k}')
                total_branco += h

    elif escolha == 3:
        print(f'Foram ao total {total_nulo} votos nulos e {total_branco} votos brancos')

    elif escolha == 4:
        for k, v in total_urna.items():
            print(f'O total de votos computados na {k} foi {v} votos.')

    elif escolha == 5:
        for k, v in num_chapasD.items():
            print(f'A chapa {k} teve {v} votos.')

    elif escolha == 6:
        for k, v in num_chapasT.items():
            print(f'A chapa {k} teve {v} votos.')

    elif escolha == 7:
        for k, v in num_chapasDI.items():
            print(f'A chapa {k} teve {v} votos.')

    elif escolha == 8:
        if ntsd == 0:
            print('Não houve ausentes na categoria servidores discentes.')
        else:
            a_ntsd = (100 * ntsd) / NTSD
            print(f'A porcentagem de asuentes da categoria servidores doscentes {a_ntsd:.2f}%')

        if ntst == 0:
            print('Não houve ausentes na categoria servidores técnicos.')
        else:
            a_ntst = (100 * ntst) / NTST
            print(f'A porcentagem de asuentes da categoria servidores técnicos {a_ntst:.2f}%')

        if ntd == 0:
            print('Não houve ausentes na categoria discentes.')
        else:
            a_ntd = (100 * ntd) / NTD
            print(f'A porcentagem de asuentes da categoria discentes {a_ntd:.2f}%')

    elif escolha == 9:
        NV = 0
        for k, v in votantesC.items():
            NV += v
            print(f'valor {NV}')
        escore = 0
        for k, v in num_chapasD.items():
            escore += (((v / NTSD) * (1 / 3)) + (((num_chapasT[k] / NTST) * (1 / 3)) + ((num_chapasDI[k] / NTD) * (1 / 3))) * NV)
            print(f'O escore da chapa {k} foi escore = {escore:.2f}')
            maior_escore = escore
            chapa_vence = k
            if escore > maior_escore:
                maior_escore = escore
                chapa_vence = k
        print(f'A chapa vencedora foi a {chapa_vence}')

    elif escolha == 10:
        break