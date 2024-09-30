from constantes import *
import motor_grafico as motor


def desenha_tela(janela, estado, altura, largura):
    motor.preenche_fundo(janela, VERDE_CLARO)

    motor.desenha_string(janela, largura // 2 - len('The Unculling') // 2, altura // 2, 'The Unculling', VERDE_CLARO, BRANCO)
    motor.desenha_string(janela, largura // 2 - len('Aperte j para iniciar o jogo!') // 2, altura // 2 + 3, 'Aperte j para iniciar o jogo!', VERDE_CLARO, BRANCO)
    motor.desenha_string(janela, largura // 2 - len('Aperte i para ler as instruções do jogo!') // 2, altura // 2 + 4, 'Aperte i para ler as instruções do jogo!', VERDE_CLARO, BRANCO)
    motor.desenha_string(janela, largura // 2 - len('Aperte ESC ou q para sair do jogo!') // 2, altura // 2 + 5, 'Aperte ESC ou q para sair do jogo!', VERDE_CLARO, BRANCO)
    motor.mostra_janela(janela)


def atualiza_estado(estado, tecla_apertada):
    if tecla_apertada in (motor.ESCAPE, 'q'):
        estado['tela_atual'] = SAIR

    elif tecla_apertada == 'j':
        estado['tela_atual'] = TELA_JOGO
    elif tecla_apertada == 'i':
        estado['tela_atual'] = TELA_INSTRUCAO