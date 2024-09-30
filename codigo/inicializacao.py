from random import randint
from constantes import *  

def gera_posicao_desocupada(posicoes_ocupadas, largura_mapa, altura_mapa):

    posicoes_ocupadas = []
    ocupada = True
    while ocupada:
        x = randint(1, largura_mapa-2)
        y = randint(1, altura_mapa-2)
        posicao = [x, y]
        if posicao not in posicoes_ocupadas:    # Se a posição gerada não estiver ocupada
            posicoes_ocupadas.append(posicao)   # Adiciona a posição à lista de posições ocupadas
            ocupada = False
    return posicao


def gera_objetos(quantidade, tipo, cor, largura_mapa, altura_mapa, posicoes_ocupadas):
    """
    Esta função já está pronta, você não precisa modificá-la.

    Gera uma lista de objetos do tipo especificado, com a quantidade especificada.
    Cada objeto é um dicionário com as chaves 'tipo', 'posicao' e 'cor'.

    Parâmetros:
    quantidade: quantidade de objetos a serem gerados
    tipo: tipo do objeto a ser gerado. É uma string como '❤'
    cor: cor do objeto a ser gerado. É uma lista com três elementos, como [255, 0, 0]
    largura_mapa: largura do mapa do jogo em caracteres
    altura_mapa: altura do mapa do jogo em caracteres
    posicoes_ocupadas: lista de posições ocupadas no mapa. Cada posição é uma lista com exatamente dois elementos: a posição x e a posição y.
    """
    lista_paredes = []
    for i in range(largura_mapa):
        lista_paredes.append([i, 0])
    for i in range(1, altura_mapa):
        lista_paredes.append([0, i])
        lista_paredes.append([largura_mapa - 1, i])
    for i in range(largura_mapa):
        lista_paredes.append([i, altura_mapa-1])
        
    objetos = []
    if tipo != PAREDE:  # Se o tipo do objeto não for parede 
        for i in range(quantidade):
            posicao = gera_posicao_desocupada(posicoes_ocupadas, largura_mapa, altura_mapa)
            if tipo != MONSTRO_1 and tipo != MONSTRO_2:
                objetos.append({    # Atributos do objeto
                    'tipo': tipo,
                    'posicao': posicao,
                    'cor': cor,
                })
            elif tipo == PESSOA:
                objetos.append({    # Atributos da pessoa
                    'tipo': tipo,
                    'posicao': posicao,
                    'cor': cor,
                    'vidas': 1,
                })
            elif tipo == MONSTRO_1:
                objetos.append({    # Atributos do monstro 1
                    'tipo': tipo,
                    'posicao': posicao,
                    'cor': cor,
                    'vidas': 5,
                    'probabilidade_de_ataque': 0.2,
                })
            elif tipo == MONSTRO_2: # Atributos do monstro 2
                objetos.append({
                    'tipo': tipo,
                    'posicao': posicao,
                    'cor': cor,
                    'vidas': 2,
                    'probabilidade_de_ataque': 0.4,
                })
    else:
        for i in range(quantidade):
            posicao = lista_paredes[i]
            posicoes_ocupadas.append(posicao)
            objetos.append({    # Atributos da parede
                'tipo': tipo,
                'posicao': posicao,
                'cor': cor,
            })

    return objetos


def inicializa_estado():
    # Cria lista de listas, cada uma com 50 espaços em branco
    mapa = [            # 90 x 30
        [' '] * 90,
        [' '] * 90,
        [' '] * 90,
        [' '] * 90,
        [' '] * 90,
        [' '] * 90,
        [' '] * 90,
        [' '] * 90,
        [' '] * 90,
        [' '] * 90,
        [' '] * 90,
        [' '] * 90,
        [' '] * 90,
        [' '] * 90,
        [' '] * 90,
        [' '] * 90,
        [' '] * 90,
        [' '] * 90,
        [' '] * 90,
        [' '] * 90,
        [' '] * 90,
        [' '] * 90,
        [' '] * 90,
        [' '] * 90,
        [' '] * 90,
        [' '] * 90,
        [' '] * 90,
        [' '] * 90,
        [' '] * 90,
        [' '] * 90,
    ]

    largura_mapa = len(mapa[0])
    altura_mapa = len(mapa)
    
    # Você pode colocar o jogador em outro lugar, se preferir
    pos_jogador = [largura_mapa//2, altura_mapa//2]  # Meio do mapa
    
    # quantidade de objetos de cada tipo
    num_paredes = 237
    num_coracoes = 8
    num_armadilhas = 8
    num_monstros_1 = 10
    num_monstros_2 = 10
    num_pessoas = 25

    posicoes_ocupadas = [pos_jogador]
    objetos = []
    # gera os objetos
    objetos += gera_objetos(num_paredes, PAREDE, MARROM_ESCURO, largura_mapa, altura_mapa, posicoes_ocupadas)
    objetos += gera_objetos(num_coracoes, CORACAO, VERMELHO, largura_mapa, altura_mapa, posicoes_ocupadas)
    objetos += gera_objetos(num_armadilhas, ARMADILHA, MARROM_ESCURO, largura_mapa, altura_mapa, posicoes_ocupadas)
    objetos += gera_objetos(num_monstros_1, MONSTRO_1, MARROM_ESCURO, largura_mapa, altura_mapa, posicoes_ocupadas)
    objetos += gera_objetos(num_monstros_2, MONSTRO_2, MARROM_ESCURO, largura_mapa, altura_mapa, posicoes_ocupadas)
    objetos += gera_objetos(num_pessoas, PESSOA, MARROM_ESCURO, largura_mapa, altura_mapa, posicoes_ocupadas)

    return {
        'tela_atual': TELA_INICIAL,
        'pos_jogador': pos_jogador,
        'vidas': 5,                         # Quantidade atual de vidas do jogador - ele pode perder vidas ao colidir com espinhos ou ganhar vidas ao pegar corações
        'max_vidas': 5,                     # Quantidade máxima de vidas que o jogador pode ter - o valor da chave 'vidas' nunca pode ser maior que o valor da chave 'max_vidas'
        'objetos': objetos,
        'mapa': mapa,
        'num_pessoas_vivas': num_pessoas,   # Número de pessoas vivas no mapa
        'max_pessoas_vivas': num_pessoas,   # Número máximo de pessoas vivas no mapa
        'inventario': [],                   # Lista de objetos que o jogador coletou
        'max_inventario': 6,                # Quantidade máxima de objetos que o jogador pode carregar
        'indice_inventario': 0,             # Índice do objeto que está selecionado no inventário
        'mensagem': '',                     # Use esta mensagem para mostrar mensagens ao jogador, como "Você perdeu uma vida" ou "Você ganhou uma vida"
        'mensagem_pessoas_vivas': '',       # Use esta mensagem para mostrar mensagens ao jogador sobre o número de pessoas vivas
    }

estado = inicializa_estado()