from constantes import *
import motor_grafico as motor
from inicializacao import gera_objetos

# função para usar um item do inventário
def usa_item(estado):
        if estado['inventario'][estado['indice_inventario']] == 'Pocao De Vida':
            usa_pocao_de_vida(estado)
        elif estado['inventario'][estado['indice_inventario']] == 'Pergaminho Da Ressureicao': 
            usa_pergaminho_da_ressureicao(estado)

# função para usar uma poção de vida
def usa_pocao_de_vida(estado):
    if estado['vidas'] < estado['max_vidas']:    
        estado['vidas'] += 1
        estado['inventario'].remove('Pocao De Vida')
        estado['mensagem'] = 'Você usou uma poção de vida!'
    else:
        estado['mensagem'] = 'Sua vida já está cheia!'
    estado['tela_atual'] = TELA_JOGO

# função para usar um pergaminho da ressureição
def usa_pergaminho_da_ressureicao(estado):
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
    
    armadilhas = []
    for dict_objetos in estado["objetos"]:
        if dict_objetos["tipo"] == ARMADILHA:
            armadilhas.append(dict_objetos["posicao"])

    posicoes_ocupadas = paredes + monstros + pessoas + armadilhas + [estado["pos_jogador"]]
    if estado['num_pessoas_vivas'] < estado['max_pessoas_vivas']:
        posicoes_ocupadas += gera_objetos(1, PESSOA, BRANCO, len(estado["mapa"][0]), len(estado["mapa"]), posicoes_ocupadas)
        estado['objetos'] += gera_objetos(1, PESSOA, BRANCO, len(estado["mapa"][0]), len(estado["mapa"]), posicoes_ocupadas) # ressucita uma pessoa
        estado['num_pessoas_vivas'] += 1
        estado['inventario'].remove('Pergaminho Da Ressureicao')
    else:
        estado['mensagem'] = 'Não há pessoas mortas!'
    estado['tela_atual'] = TELA_JOGO

def desenha_tela(janela, estado, altura, largura):

    motor.preenche_fundo(janela, BRANCO)

    motor.desenha_string(janela, 1, 1, 'INVENTARIO', BRANCO, PRETO)
    motor.desenha_string(janela, 1, 2, '----------', BRANCO, PRETO)
    for i, item in enumerate(estado['inventario']):
        if i == estado['indice_inventario']:
            motor.desenha_string(janela, 1, 3 + i, f"   {item}", BRANCO, VERMELHO)  # Faz o destaque do item selecionado
        else:
            motor.desenha_string(janela, 1, 3 + i, item, BRANCO, PRETO)
    motor.mostra_janela(janela)


def atualiza_estado(estado, tecla_apertada):
    if tecla_apertada == "u": # u para usar o item selecionado
        usa_item(estado)

    elif tecla_apertada == motor.SETA_CIMA and estado['indice_inventario'] != 0:
        estado['indice_inventario'] -= 1

    elif tecla_apertada == motor.SETA_BAIXO and estado['indice_inventario'] != len(estado['inventario']) - 1:
        estado['indice_inventario'] += 1
                
    elif tecla_apertada in (motor.ESCAPE, 'q'):
        estado['tela_atual'] = SAIR
        
    elif tecla_apertada == 'i':
        estado['tela_atual'] = TELA_JOGO