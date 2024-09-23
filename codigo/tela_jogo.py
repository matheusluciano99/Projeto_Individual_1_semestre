from constantes import *  # Você pode usar as constantes definidas em constantes.py, se achar útil
                          # Por exemplo, usar a constante CORACAO é o mesmo que colocar a string '❤'
                          # diretamente no código
import motor_grafico as motor  # Utilize as funções do arquivo motor_grafico.py para desenhar na tela
                               # Por exemplo: motor.preenche_fundo(janela, [0, 0, 0]) preenche o fundo de preto


def desenha_tela(janela, estado, altura_tela, largura_tela):
    # Utilize o dicionário estado para saber onde o jogador e os outros objetos estão.
    
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
                motor.desenha_string(janela, x + 30, y + 5, " ", VERDE_CLARO, BRANCO)

        for dict_objetos in estado["objetos"]:
            motor.desenha_string(janela, dict_objetos["posicao"][0] + 30, dict_objetos["posicao"][1] + 5, dict_objetos["tipo"], VERDE_CLARO, PRETO)

        motor.desenha_string(janela, estado["pos_jogador"][0] + 30, estado["pos_jogador"][1] + 5, JOGADOR, VERDE_CLARO, PRETO)
        motor.desenha_string(janela, 0, len(estado["mapa"]) + 10, estado["mensagem"], PRETO, BRANCO)

    elif estado["tela_atual"] == TELA_GAME_OVER:
        for x in range(len(estado["mapa"][0])):
            motor.desenha_string(janela, x, len(estado["mapa"]) // 2, "GAME_OVER", PRETO, BRANCO)

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
    if estado["pos_jogador"][1] != 0:
        if tecla == motor.SETA_CIMA:
            estado["pos_jogador"][1] -= 1

    if estado["pos_jogador"][0] != 0:
        if tecla == motor.SETA_ESQUERDA:
            estado["pos_jogador"][0] -= 1
    if estado["pos_jogador"][1] != len(estado["mapa"]) - 1:
        if tecla == motor.SETA_BAIXO:
            estado["pos_jogador"][1] += 1

    if estado["pos_jogador"][0] != len(estado["mapa"][0]) - 1:
        if tecla == motor.SETA_DIREITA:
            estado["pos_jogador"][0] += 1

    i = 0
    for dict_objetos in estado["objetos"]:
        
        if estado["pos_jogador"] == dict_objetos["posicao"] and dict_objetos["tipo"] == COCO:
            estado['mensagem'] = 'Você pisou no cocô do cavalo!'
            estado["vidas"] -= 1

        elif estado["pos_jogador"] == dict_objetos["posicao"] and dict_objetos["tipo"] == CAVALO:
            estado['mensagem'] = 'Você tomou um coice do cavalo!'
            estado["vidas"] -= 1

        elif estado["pos_jogador"] == dict_objetos["posicao"] and dict_objetos["tipo"] == CORACAO:
            if estado["vidas"] != estado["max_vidas"]:
                estado["vidas"] += 1
                estado['mensagem'] = 'Você ganhou uma vida!'
                del estado["objetos"][i]
            else:
                estado['mensagem'] = 'Você está com vida máxima!'
        i+=1

    if estado["vidas"] == 0:
        estado["tela_atual"] = TELA_GAME_OVER

    # Ao apertar a tecla 'i', o jogador deve ver o inventário
    if tecla == 'i':
        estado['tela_atual'] = TELA_INVENTARIO
    # Termina o jogo se o jogador apertar ESC ou 'q'
    elif tecla == motor.ESCAPE or tecla =='q':
        estado['tela_atual'] = SAIR