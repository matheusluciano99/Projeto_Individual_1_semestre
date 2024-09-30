[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/gn9YUziy)
# [The Unculling]

Este é um projeto de um jogo [roguelike](https://pt.wikipedia.org/wiki/Roguelike) desenvolvido por Matheus Luciano como projeto individual na disciplina Developer Life do semestre do curso de Ciência da Computação do Insper. O jogo foi desenvolvido em Python, utilizando o módulo [curses](https://docs.python.org/3/library/curses.html) para a interface gráfica. 

## Descrição do jogo

O roguelike desenvolvido consiste em um jogo, de exploração de uma cidade que está sendo invadida por monstros, inspirado pelo capítulo "The Culling" do jogo Warcraft 3: Reign of Chaos, onde o jogador controla um personagem e deve derrotar os monstros e coletar tesouros antes que os monstros expurguem a cidade ou você morra. 

O jogo apresenta alguns elementos característicos de roguelikes, como morte permanente (permadeath) e combates baseados em turnos.

## Como jogar

Para jogar, é necessário ter o Python 3 instalado na máquina. Além disso, se você estiver no Windows, consulte o [guia abaixo](#jogando-no-windows) para mais informações.

Após instalar a biblioteca, clone este repositório e execute o arquivo `jogo.py`, dentro da pasta `codigo`. O jogo será aberto em uma janela de terminal e pode ser jogado com as seguintes teclas:

- **Movimento**: teclas de seta
- **Fechar jogo**: tecla "esc"

### Jogando no Windows

No Windows é necessário instalar algumas dependências adicionais. O módulo utilizado por este projeto pode não funcionar corretamente com o prompt de comando padrão do Windows. Por esse motivo, comece instalando o Windows Terminal. Para isso, siga [estes passos de instalação](https://learn.microsoft.com/pt-br/windows/terminal/install).

Com o Windows Terminal instalado, precisamos instalar também o módulo `windows-curses`, utilizando o gerenciador de pacotes pip. Para isso, abra o terminal e execute o seguinte comando:

```bash
pip install windows-curses
```

Pronto! Agora você pode seguir os passos da seção ["Como jogar"](#como-jogar) para executar o jogo.

## Outros links

- [Enunciado do projeto](docs/enunciado.md)
- [Funcionalidades implementadas](docs/funcionalidades-implementadas.md)
- [Documentação das funções fornecidas pelos professores](codigo/motor_grafico/README.md)