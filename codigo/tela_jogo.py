from constantes import *  # Você pode usar as constantes definidas em constantes.py, se achar útil
                          # Por exemplo, usar a constante CORACAO é o mesmo que colocar a string '❤'
                          # diretamente no código
import motor_grafico as motor  # Utilize as funções do arquivo motor_grafico.py para desenhar na tela
                               # Por exemplo: motor.preenche_fundo(janela, [0, 0, 0]) preenche o fundo de preto
from random import randint, random

def combate(estado):
    ataque_jogador = random()
    for dict_objetos in estado["objetos"]:
        if dict_objetos["tipo"] == MONSTRO and estado["pos_jogador"] == dict_objetos["posicao"]:
            if ataque_jogador < dict_objetos["probabilidade_de_ataque"]:
                estado["vidas"] -= 1
                estado["mensagem"] = f"O monstro te atacou! Ele tem {dict_objetos['vidas']} vidas!"
            else:
                dict_objetos["vidas"] -= 1
                if dict_objetos["vidas"] == 0:
                    estado["pos_jogador"] = dict_objetos["posicao"]
                    estado["mensagem"] = "Você matou o monstro!"
                    estado["objetos"].remove(dict_objetos)
                else:
                    estado["mensagem"] = f"Você atacou o monstro! Ele tem {dict_objetos['vidas']} vidas!"

def movimentacao_monstro(estado):
    
    dict_comandos = { 
                        0: motor.SETA_CIMA,
                        1: motor.SETA_BAIXO, 
                        2: motor.SETA_ESQUERDA, 
                        3: motor.SETA_DIREITA
                    }

    paredes = []
    for dict_objetos in estado["objetos"]:
        if dict_objetos["tipo"] == PAREDE:
            paredes.append(dict_objetos["posicao"])

    for dict_objetos in estado["objetos"]:
        num_comando = randint(0, 3)
        if dict_objetos["tipo"] == MONSTRO:
            if num_comando == 0:
                dict_objetos["posicao"][1] -= 1
                if dict_objetos["posicao"] in paredes:
                    dict_objetos["posicao"][1] += 1
                elif dict_objetos["posicao"] == estado["pos_jogador"]:
                    dict_objetos["posicao"][1] += 1

            elif num_comando == 1:
                dict_objetos["posicao"][1] += 1
                if dict_objetos["posicao"] in paredes:
                    dict_objetos["posicao"][1] -= 1
                elif dict_objetos["posicao"] == estado["pos_jogador"]:
                    dict_objetos["posicao"][1] -= 1

            elif num_comando == 2:
                dict_objetos["posicao"][0] -= 1
                if dict_objetos["posicao"] in paredes:
                    dict_objetos["posicao"][0] += 1
                elif dict_objetos["posicao"] == estado["pos_jogador"]:
                    dict_objetos["posicao"][0] += 1

            elif num_comando == 3:
                dict_objetos["posicao"][0] += 1
                if dict_objetos["posicao"] in paredes:
                    dict_objetos["posicao"][0] -= 1
                elif dict_objetos["posicao"] == estado["pos_jogador"]:
                    dict_objetos["posicao"][0] -= 1
    
def movimentacao(estado, tecla):
    paredes = []
    for dict_objetos in estado["objetos"]:
        if dict_objetos["tipo"] == PAREDE:
            paredes.append(dict_objetos["posicao"])

    monstros = []
    for dict_objetos in estado["objetos"]:
        if dict_objetos["tipo"] == MONSTRO:
            monstros.append(dict_objetos["posicao"])

    if tecla == motor.SETA_CIMA:
        estado["pos_jogador"][1] -= 1
        if estado["pos_jogador"] in paredes:
            estado["mensagem"] = "Você não pode passar pela parede!"
            estado["pos_jogador"][1] += 1
        elif estado["pos_jogador"] in monstros:
            combate(estado)
            if estado["mensagem"] != "Você matou o monstro!":
                estado["pos_jogador"][1] += 1
            

    if tecla == motor.SETA_ESQUERDA:
        estado["pos_jogador"][0] -= 1
        if estado["pos_jogador"] in paredes:
            estado["mensagem"] = "Você não pode passar pela parede!"
            estado["pos_jogador"][0] += 1
        elif estado["pos_jogador"] in monstros:
            combate(estado)
            if estado["mensagem"] != "Você matou o monstro!":
                estado["pos_jogador"][0] += 1

    if tecla == motor.SETA_BAIXO:
        estado["pos_jogador"][1] += 1
        if estado["pos_jogador"] in paredes:
            estado["mensagem"] = "Você não pode passar pela parede!"
            estado["pos_jogador"][1] -= 1
        elif estado["pos_jogador"] in monstros:
            combate(estado)
            if estado["mensagem"] != "Você matou o monstro!":
                estado["pos_jogador"][1] -= 1

    if tecla == motor.SETA_DIREITA:
        estado["pos_jogador"][0] += 1
        if estado["pos_jogador"] in paredes:
            estado["mensagem"] = "Você não pode passar pela parede!"
            estado["pos_jogador"][0] -= 1
        elif estado["pos_jogador"] in monstros:
            combate(estado)
            if estado["mensagem"] != "Você matou o monstro!":
                estado["pos_jogador"][0] -= 1

    for dict_objetos in estado["objetos"]:
        
        if estado["pos_jogador"] == dict_objetos["posicao"] and dict_objetos["tipo"] == ESPINHO:
            estado['mensagem'] = 'Você caiu no espinho!'
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
    # Por exemplo, para saber a posição do jogador, use estado['pos_jogador']
    # O mapa esta armazenado em estado['mapa'].
    motor.preenche_fundo(janela, PRETO)
    
    # O seu código deve desenhar a tela do jogo aqui a partir dos valores no dicionário "estado"
    if estado["tela_atual"] == TELA_JOGO:
        for x in range(0, 2 * estado["vidas"], 2):
            motor.desenha_string(janela, x, 0, CORACAO, PRETO, BRANCO)

        for x in range(2 * estado["vidas"], 2 * estado["max_vidas"], 2):
            motor.desenha_string(janela, x, 0, CORACAO_VAZIO, PRETO, BRANCO)

        for x in range(len(estado["mapa"][0])):
            for y in range(len(estado["mapa"])):
                motor.desenha_string(janela, x + posicao_ajustada_x, y + posicao_ajustada_y, " ", VERDE_CLARO, BRANCO)

        for dict_objetos in estado["objetos"]:
            motor.desenha_string(janela, dict_objetos["posicao"][0] + posicao_ajustada_x, dict_objetos["posicao"][1] + posicao_ajustada_y, dict_objetos["tipo"], VERDE_CLARO, PRETO)

        motor.desenha_string(janela, estado["pos_jogador"][0] + posicao_ajustada_x, estado["pos_jogador"][1] + posicao_ajustada_y, JOGADOR, VERDE_CLARO, PRETO)
        motor.desenha_string(janela, 0, altura_tela - 1, estado["mensagem"], PRETO, BRANCO)

    motor.mostra_janela(janela)
    

def atualiza_estado(estado, tecla):
    # O seu código deve atualizar o dicionário "estado" com base na tecla apertada pelo jogador
    # Por exemplo, se o jogador apertar a seta para a esquerda (o valor da variável será "ESQUERDA"), 
    # o seu código deve atualizar o dicionário estado['pos_jogador'][0] -= 1

    # Mude o valor da chave 'tela_atual' para mudar de tela
    
    # Começamos apagando a mensagem anterior, pois ela já foi mostrada no frame anterior
    estado["mensagem"] = ""
                

    # Escreva seu código para atualizar o dicionário "estado" com base na tecla apertada pelo jogador aqui
    # APAGUE ESTA LINHA E ESCREVA SEU CÓDIGO AQUI
    movimentacao(estado, tecla)
    movimentacao_monstro(estado)
    if estado["vidas"] == 0:
        estado["tela_atual"] = TELA_GAME_OVER

    # Ao apertar a tecla 'i', o jogador deve ver o inventário
    if tecla == 'i':
        estado['tela_atual'] = TELA_INVENTARIO
    # Termina o jogo se o jogador apertar ESC ou 'q'
    elif tecla == motor.ESCAPE or tecla =='q':
        estado['tela_atual'] = SAIR

    