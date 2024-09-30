from constantes import *
import motor_grafico as motor


def desenha_tela(janela, estado, altura, largura):

    motor.preenche_fundo(janela, VERDE_CLARO)

    motor.desenha_string(janela, largura // 2 - len('VOCÊ MORREU!') // 2, altura // 2, 'VOCÊ MORREU!', VERDE_CLARO, BRANCO)
    motor.mostra_janela(janela)


def atualiza_estado(estado, tecla_apertada):
    if tecla_apertada in (motor.ESCAPE, 'q'):
        estado['tela_atual'] = SAIR