from constantes import *  
import motor_grafico as motor
from random import randint, random

# função para drop de item
def drop_item(estado):
    dict_item_probabilidade = {
        'pocao_de_vida': 0.3,
        'pergaminho_da_ressureicao': 0.15,
    }

    for item, chance_de_drop in dict_item_probabilidade.items():
        if len(estado['inventario']) == estado['max_inventario'] and random() < chance_de_drop:
            estado['mensagem'] = "Seu inventário está cheio!"
            break   # se o inventário estiver cheio, não dropa o item
        elif random() < chance_de_drop:
            estado['inventario'].append(item.replace('_', ' ').title())
            estado['mensagem'] = f"Você matou o monstro e obteve um(a) {item.replace('_', ' ').title()}!"
            break   # se o item for dropado, não dropa outro item

# função para o combate entre o jogador e os monstros
def combate(estado):
    ataque_jogador = random()
    for dict_objetos in estado["objetos"]:
        if (dict_objetos["tipo"] == MONSTRO_1 or dict_objetos["tipo"] == MONSTRO_2) and estado["pos_jogador"] == dict_objetos["posicao"]:
            if ataque_jogador < dict_objetos["probabilidade_de_ataque"]:
                estado["vidas"] -= 1
                estado["mensagem"] = f"O monstro te atacou! Ele tem {dict_objetos['vidas']} vidas!"
            else:
                dict_objetos["vidas"] -= 1
                if dict_objetos["vidas"] == 0:
                    estado["pos_jogador"] = dict_objetos["posicao"]
                    estado["mensagem"] = "Você matou o monstro!"
                    drop_item(estado)
                    estado["objetos"].remove(dict_objetos)
                else:
                    estado["mensagem"] = f"Você atacou o monstro! Ele tem {dict_objetos['vidas']} vidas!"

# função para o monstro atacar as pessoas
def interacao_pessoa_monstro(estado):
    monstros = []
    for dict_objetos in estado["objetos"]:
        if dict_objetos["tipo"] == MONSTRO_1 or dict_objetos["tipo"] == MONSTRO_2:
            monstros.append(dict_objetos["posicao"])
    
    for dict_objetos in estado["objetos"]:
        if dict_objetos["tipo"] == PESSOA:
            if dict_objetos["posicao"] in monstros:
                estado["objetos"].remove(dict_objetos)
                estado["num_pessoas_vivas"] -= 1
                estado["mensagem"] = "Uma pessoa foi morta por um monstro!"

# função para as pessoas morrerem nas armadilhas
def interacao_pessoa_armadilha(estado):
    armadilhas = []
    for dict_objetos in estado["objetos"]:
        if dict_objetos["tipo"] == ARMADILHA:
            armadilhas.append(dict_objetos["posicao"])

    for dict_objetos in estado["objetos"]:
        if dict_objetos["tipo"] == PESSOA:
            if dict_objetos["posicao"] in armadilhas:
                estado["objetos"].remove(dict_objetos)
                estado["num_pessoas_vivas"] -= 1
                estado["mensagem"] = "Uma pessoa morreu em uma armadilha!"

# movimentação das pessoas
def movimentacao_pessoa(estado):
    paredes = []
    for dict_objetos in estado["objetos"]:
        if dict_objetos["tipo"] == PAREDE:
            paredes.append(dict_objetos["posicao"])

    pessoas = []
    for dict_objetos in estado["objetos"]:
        if dict_objetos["tipo"] == PESSOA:
            pessoas.append(dict_objetos["posicao"])

    monstros = []
    for dict_objetos in estado["objetos"]:
        if dict_objetos["tipo"] == MONSTRO_1 or dict_objetos["tipo"] == MONSTRO_2:
            monstros.append(dict_objetos["posicao"])

    armadilhas = []
    for dict_objetos in estado["objetos"]:
        if dict_objetos["tipo"] == ARMADILHA:
            armadilhas.append(dict_objetos["posicao"])

    dict_comandos = {
                        0: motor.SETA_CIMA,
                        1: motor.SETA_BAIXO, 
                        2: motor.SETA_ESQUERDA, 
                        3: motor.SETA_DIREITA
                    }

    for dict_objetos in estado["objetos"]:
        if dict_objetos["tipo"] == PESSOA:
            comando = dict_comandos[randint(0, 3)]
            posicao_original = dict_objetos["posicao"]
            pessoas.remove(posicao_original) # remove a posição original da pessoa da lista de pessoas

            if comando == motor.SETA_CIMA:
                dict_objetos["posicao"][1] -= 1
                if dict_objetos["posicao"] in paredes or dict_objetos["posicao"] == estado["pos_jogador"] or dict_objetos["posicao"] in pessoas:
                    dict_objetos["posicao"][1] += 1
                elif dict_objetos["posicao"] in armadilhas:
                    interacao_pessoa_armadilha(estado)
                elif dict_objetos["posicao"] in monstros:
                    interacao_pessoa_monstro(estado)

            elif comando == motor.SETA_BAIXO:
                dict_objetos["posicao"][1] += 1
                if dict_objetos["posicao"] in paredes or dict_objetos["posicao"] == estado["pos_jogador"] or dict_objetos["posicao"] in pessoas:
                    dict_objetos["posicao"][1] -= 1
                elif dict_objetos["posicao"] in armadilhas:
                    interacao_pessoa_armadilha(estado)
                elif dict_objetos["posicao"] in monstros:
                    interacao_pessoa_monstro(estado)

            elif comando == motor.SETA_ESQUERDA:
                dict_objetos["posicao"][0] -= 1
                if dict_objetos["posicao"] in paredes or dict_objetos["posicao"] == estado["pos_jogador"] or dict_objetos["posicao"] in pessoas:
                    dict_objetos["posicao"][0] += 1
                elif dict_objetos["posicao"] in armadilhas:
                    interacao_pessoa_armadilha(estado)
                elif dict_objetos["posicao"] in monstros:
                    interacao_pessoa_monstro(estado)

            elif comando == motor.SETA_DIREITA:
                dict_objetos["posicao"][0] += 1
                if dict_objetos["posicao"] in paredes or dict_objetos["posicao"] == estado["pos_jogador"] or dict_objetos["posicao"] in pessoas:
                    dict_objetos["posicao"][0] -= 1
                elif dict_objetos["posicao"] in armadilhas:
                    interacao_pessoa_armadilha(estado)
                elif dict_objetos["posicao"] in monstros:
                    interacao_pessoa_monstro(estado)
            
            pessoas.append(dict_objetos["posicao"]) # anexa a posição atual da pessoa na lista de pessoas
    
# movimentação dos monstros
def movimentacao_monstro(estado):
    paredes = []
    for dict_objetos in estado["objetos"]:
        if dict_objetos["tipo"] == PAREDE:
            paredes.append(dict_objetos["posicao"])

    armadilhas = []
    for dict_objetos in estado["objetos"]:
        if dict_objetos["tipo"] == ARMADILHA:
            armadilhas.append(dict_objetos["posicao"])

    pessoas = []
    for dict_objetos in estado["objetos"]:
        if dict_objetos["tipo"] == PESSOA:
            pessoas.append(dict_objetos["posicao"])
    
    monstros = []
    for dict_objetos in estado["objetos"]:
        if dict_objetos["tipo"] == MONSTRO_1 or dict_objetos["tipo"] == MONSTRO_2:
            monstros.append(dict_objetos["posicao"])

    dict_comandos = { 
                        0: motor.SETA_CIMA,
                        1: motor.SETA_BAIXO, 
                        2: motor.SETA_ESQUERDA, 
                        3: motor.SETA_DIREITA
                    }

    for dict_objetos in estado["objetos"]:
        if dict_objetos["tipo"] == MONSTRO_1 or dict_objetos["tipo"] == MONSTRO_2:
            comando = dict_comandos[randint(0, 3)]
            posicao_original = dict_objetos["posicao"]
            monstros.remove(posicao_original) # remove a posição original do monstro da lista de monstros

            if comando == motor.SETA_CIMA:
                dict_objetos["posicao"][1] -= 1
                if dict_objetos["posicao"] in paredes or dict_objetos["posicao"] == estado["pos_jogador"] or dict_objetos["posicao"] in armadilhas or dict_objetos["posicao"] in monstros:
                    dict_objetos["posicao"][1] += 1

            elif comando == motor.SETA_BAIXO:
                dict_objetos["posicao"][1] += 1
                if dict_objetos["posicao"] in paredes or dict_objetos["posicao"] == estado["pos_jogador"] or dict_objetos["posicao"] in armadilhas or dict_objetos["posicao"] in monstros:
                    dict_objetos["posicao"][1] -= 1

            elif comando == motor.SETA_ESQUERDA:
                dict_objetos["posicao"][0] -= 1
                if dict_objetos["posicao"] in paredes or dict_objetos["posicao"] == estado["pos_jogador"] or dict_objetos["posicao"] in armadilhas or dict_objetos["posicao"] in monstros:
                    dict_objetos["posicao"][0] += 1

            elif comando == motor.SETA_DIREITA:
                dict_objetos["posicao"][0] += 1
                if dict_objetos["posicao"] in paredes or dict_objetos["posicao"] == estado["pos_jogador"] or dict_objetos["posicao"] in armadilhas or dict_objetos["posicao"] in monstros:
                    dict_objetos["posicao"][0] -= 1

        monstros.append(dict_objetos["posicao"]) # anexa a posição atual do monstro na lista de monstros
    
# movimentação do jogador
def movimentacao(estado, tecla):
    paredes = []
    for dict_objetos in estado["objetos"]:
        if dict_objetos["tipo"] == PAREDE:
            paredes.append(dict_objetos["posicao"])

    monstros = []
    for dict_objetos in estado["objetos"]:
        if dict_objetos["tipo"] == MONSTRO_1 or dict_objetos["tipo"] == MONSTRO_2:
            monstros.append(dict_objetos["posicao"])

    pessoas = []
    for dict_objetos in estado["objetos"]:
        if dict_objetos["tipo"] == PESSOA:
            pessoas.append(dict_objetos["posicao"])

    
    if tecla == motor.SETA_CIMA:
        estado["pos_jogador"][1] -= 1
        if estado["pos_jogador"] in paredes:
            estado["mensagem"] = "Você não pode passar pela parede!"
            estado["pos_jogador"][1] += 1
        elif estado["pos_jogador"] in monstros:
            combate(estado)
            if "Você matou o monstro" not in estado["mensagem"]:
                estado["pos_jogador"][1] += 1
        elif estado["pos_jogador"] in pessoas:
            estado["pos_jogador"][1] += 1
            estado["mensagem"] = "Você se encontrou com uma pessoa. Ela está pedindo ajuda!"
            

    if tecla == motor.SETA_ESQUERDA:
        estado["pos_jogador"][0] -= 1
        if estado["pos_jogador"] in paredes:
            estado["mensagem"] = "Você não pode passar pela parede!"
            estado["pos_jogador"][0] += 1
        elif estado["pos_jogador"] in monstros:
            combate(estado)
            if "Você matou o monstro" not in estado["mensagem"]:
                estado["pos_jogador"][0] += 1
        elif estado["pos_jogador"] in pessoas:
            estado["pos_jogador"][0] += 1
            estado["mensagem"] = "Você se encontrou com uma pessoa. Ela está pedindo ajuda!"

    if tecla == motor.SETA_BAIXO:
        estado["pos_jogador"][1] += 1
        if estado["pos_jogador"] in paredes:
            estado["mensagem"] = "Você não pode passar pela parede!"
            estado["pos_jogador"][1] -= 1
        elif estado["pos_jogador"] in monstros:
            combate(estado)
            if "Você matou o monstro" not in estado["mensagem"]:
                estado["pos_jogador"][1] -= 1
        elif estado["pos_jogador"] in pessoas:
            estado["pos_jogador"][1] -= 1
            estado["mensagem"] = "Você se encontrou com uma pessoa. Ela está pedindo ajuda!"

    if tecla == motor.SETA_DIREITA:
        estado["pos_jogador"][0] += 1
        if estado["pos_jogador"] in paredes:
            estado["mensagem"] = "Você não pode passar pela parede!"
            estado["pos_jogador"][0] -= 1
        elif estado["pos_jogador"] in monstros:
            combate(estado)
            if "Você matou o monstro" not in estado["mensagem"]:
                estado["pos_jogador"][0] -= 1
        elif estado["pos_jogador"] in pessoas:
            estado["pos_jogador"][0] -= 1
            estado["mensagem"] = "Você se encontrou com uma pessoa. Ela está pedindo ajuda!"

    for dict_objetos in estado["objetos"]:
        
        if estado["pos_jogador"] == dict_objetos["posicao"] and dict_objetos["tipo"] == ARMADILHA:
            estado['mensagem'] = 'Você caiu na armadilha!'
            estado["vidas"] -= 1

        elif estado["pos_jogador"] == dict_objetos["posicao"] and dict_objetos["tipo"] == CORACAO:
            if estado["vidas"] != estado["max_vidas"]:
                estado["vidas"] += 1
                estado['mensagem'] = 'Você ganhou uma vida!'
                estado["objetos"].remove(dict_objetos)
            else:
                estado['mensagem'] = 'Você está com vida máxima!'

def desenha_tela(janela, estado, altura_tela, largura_tela):
    # Utilize o dicionário estado para saber onde o jogador e os outros objetos estão.
    posicao_ajustada_x = largura_tela // 2 - len(estado["mapa"][0]) // 2
    posicao_ajustada_y = altura_tela // 2 - len(estado["mapa"]) // 2
    
    motor.preenche_fundo(janela, PRETO)
    
    # Mensagem de quantas pessoas estão vivas
    estado["mensagem_pessoas_vivas"] = f"Pessoas vivas no mapa: {estado['num_pessoas_vivas']}"
    
    # O seu código deve desenhar a tela do jogo aqui a partir dos valores no dicionário "estado"
    if estado["tela_atual"] == TELA_JOGO:
        # desenha as vidas do jogador
        for x in range(0, 2 * estado["vidas"], 2):
            motor.desenha_string(janela, x, 0, CORACAO, PRETO, BRANCO)

        # desenha os corações vazios
        for x in range(2 * estado["vidas"], 2 * estado["max_vidas"], 2):
            motor.desenha_string(janela, x, 0, CORACAO_VAZIO, PRETO, BRANCO)

        for x in range(len(estado["mapa"][0])):
            for y in range(len(estado["mapa"])):
                motor.desenha_string(janela, x + posicao_ajustada_x, y + posicao_ajustada_y, " ", VERDE_CLARO, BRANCO)

        for dict_objetos in estado["objetos"]:
            motor.desenha_string(janela, dict_objetos["posicao"][0] + posicao_ajustada_x, dict_objetos["posicao"][1] + posicao_ajustada_y, dict_objetos["tipo"], VERDE_CLARO, PRETO)

        motor.desenha_string(janela, estado["pos_jogador"][0] + posicao_ajustada_x, estado["pos_jogador"][1] + posicao_ajustada_y, JOGADOR, VERDE_CLARO, PRETO)
        motor.desenha_string(janela, 0, altura_tela - 1, estado["mensagem"], PRETO, BRANCO)
        motor.desenha_string(janela, posicao_ajustada_x, posicao_ajustada_y - 1, estado["mensagem_pessoas_vivas"], PRETO, BRANCO)

    motor.mostra_janela(janela)
    

def atualiza_estado(estado, tecla):

    lista_pessoas_vivas = []
    for dict_objetos in estado["objetos"]:
        if dict_objetos["tipo"] == PESSOA:
            lista_pessoas_vivas.append(dict_objetos)
    numero_pessoas_vivas = len(lista_pessoas_vivas)
    estado["mensagem_pessoas_vivas"] = f"Pessoas vivas no mapa: {numero_pessoas_vivas}"
    
    estado["mensagem"] = ""

    # bloco de movimentação
    movimentacao(estado, tecla)
    movimentacao_monstro(estado)
    movimentacao_pessoa(estado)

    # se o jogador morrer, a tela de morte é mostrada
    if estado["vidas"] == 0:
        estado["tela_atual"] = TELA_MORTE
    # se todas as pessoas morrerem, a tela de mission failed é mostrada
    elif numero_pessoas_vivas == 0:
        estado["tela_atual"] = TELA_MISSION_FAILED

    # Ao apertar a tecla 'i', o jogador deve ver o inventário
    if tecla == 'i':
        estado['tela_atual'] = TELA_INVENTARIO 
    # Termina o jogo se o jogador apertar ESC ou 'q'
    elif tecla == motor.ESCAPE or tecla =='q':
        estado['tela_atual'] = SAIR

    