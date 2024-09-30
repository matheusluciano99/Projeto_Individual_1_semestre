from constantes import *
import motor_grafico as motor

def desenha_tela(janela, estado, altura, largura):

    motor.preenche_fundo(janela, VERDE_CLARO)
    
    # Escreve as instruções na tela
    motor.desenha_string(janela, largura // 2 - len('Defenda a população dos monstros') // 2, altura // 2, 'Defenda a população dos monstros!', VERDE_CLARO, BRANCO)
    motor.desenha_string(janela, largura // 2 - len('A movimentação ocorre por meio das setas.') // 2, altura // 2 + 3, 'A movimentação ocorre por meio das setas', VERDE_CLARO, BRANCO)
    motor.desenha_string(janela, largura // 2 - len('Para acessar o inventario, pressione i.') // 2, altura // 2 + 4, 'Para acessar o inventario, pressione i.', VERDE_CLARO, BRANCO)
    motor.desenha_string(janela, largura // 2 - len('Ao matar um monstro, há uma chance de dropar um item. Para usá-lo, pressione "u" no item selecionado.') // 2, altura // 2 + 5, 'Ao matar um monstro, há uma chance de dropar um item. Para usá-lo, pressione "u" no item selecionado.', VERDE_CLARO, BRANCO)
    motor.desenha_string(janela, largura // 2 - len('Aperte ESC, q ou v para voltar à tela inicial.') // 2, altura // 2 + 6, 'Aperte ESC, q ou v para voltar à tela inicial.', VERDE_CLARO, BRANCO)
    motor.mostra_janela(janela)


def atualiza_estado(estado, tecla_apertada):
    if tecla_apertada in (motor.ESCAPE, 'q', 'v'):
        estado['tela_atual'] = TELA_INICIAL