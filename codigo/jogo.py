import motor_grafico
import tela_inventario
import tela_jogo
import tela_morte
import tela_mission_failed
import tela_inicial
import tela_instrucoes
from constantes import SAIR, TELA_INVENTARIO, TELA_JOGO, TELA_MORTE, TELA_MISSION_FAILED, TELA_INICIAL, TELA_INSTRUCAO
from inicializacao import inicializa_estado


def jogo(janela, altura_tela, largura_tela):
    '''
    Esta é a porta de entrada do jogo.
    Você não precisa chamar esta função. Ela será chamada pelo código
    no final deste arquivo.

    A janela é um estrutura de dados que guarda diversas informações
    sobre uma janela do jogo. A princípio você não precisa entender
    o que ela guarda, mas você deverá passar essa janela como argumento
    para as outras funções que recebem uma janela.
    '''
    estado = inicializa_estado()

    while estado['tela_atual'] != SAIR:
        # O jogo funciona como se fosse um loop infinito, que só termina quando o jogador
        # aperta a tecla 'q' ou 'esc' ou quando o jogo termina.
        # A cada iteração do loop, o jogo desenha uma tela e atualiza o estado do jogo.
        # A função pega_tecla_apertada é semelhante a uma função input(): ela espera que o
        # jogador aperte uma tecla e retorna qual tecla foi apertada. Enquanto o jogador não
        # apertar uma tecla, a função fica travada.
        
        # A função atualiza_estado é responsável por modificar o valor na chave 'tela_atual',
        # que é a chave que controla qual tela deve ser desenhada (ou se o jogo deve terminar)
        
        if estado['tela_atual'] == TELA_INICIAL:                        # desenha a tela inicial
            tela_inicial.desenha_tela(janela, estado, altura_tela, largura_tela)
            tecla_apertada = motor_grafico.pega_tecla_apertada(janela)
            tela_inicial.atualiza_estado(estado, tecla_apertada)

        elif estado['tela_atual'] == TELA_INSTRUCAO:                    # desenha a tela de instruções
            tela_instrucoes.desenha_tela(janela, estado, altura_tela, largura_tela)
            tecla_apertada = motor_grafico.pega_tecla_apertada(janela)
            tela_instrucoes.atualiza_estado(estado, tecla_apertada)
        
        elif estado['tela_atual'] == TELA_JOGO:                         # desenha a tela do jogo
            tela_jogo.desenha_tela(janela, estado, altura_tela, largura_tela)
            tecla_apertada = motor_grafico.pega_tecla_apertada(janela)
            tela_jogo.atualiza_estado(estado, tecla_apertada)
        
        elif estado['tela_atual'] == TELA_INVENTARIO:                   # desenha a tela de inventário
            tela_inventario.desenha_tela(janela, estado, altura_tela, largura_tela)
            tecla_apertada = motor_grafico.pega_tecla_apertada(janela)
            tela_inventario.atualiza_estado(estado, tecla_apertada)
        
        elif estado['tela_atual'] == TELA_MORTE:                        # desenha a tela de morte
            tela_morte.desenha_tela(janela, estado, altura_tela, largura_tela)
            tecla_apertada = motor_grafico.pega_tecla_apertada(janela)
            tela_morte.atualiza_estado(estado, tecla_apertada)
        
        elif estado['tela_atual'] == TELA_MISSION_FAILED:               # desenha a tela de mission failed
            tela_mission_failed.desenha_tela(janela, estado, altura_tela, largura_tela)
            tecla_apertada = motor_grafico.pega_tecla_apertada(janela)
            tela_mission_failed.atualiza_estado(estado, tecla_apertada)
        

# Não se preocupe, você não precisa entender o que está acontecendo aqui.
# É apenas uma forma de chamar a função jogo() usando a biblioteca curses.
motor_grafico.chama_funcao_jogo(jogo)