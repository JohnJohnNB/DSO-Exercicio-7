from AbstractControladorJogo import *
from Personagem import Personagem
from Carta import Carta
import random


class ControladorJogo(AbstractControladorJogo):
    def __init__(self):
        self.__lista_personagens = []
        self.__baralho = []

    @property
    def baralho(self) -> list:
        return self.__baralho

    @property
    def personagems(self) -> list:
        return self.__lista_personagens

    def inclui_personagem_na_lista(self,
                                   energia: int,
                                   habilidade: int,
                                   velocidade: int,
                                   resistencia: int,
                                   tipo: Tipo) -> Personagem:
        personagem_novo = Personagem(energia, habilidade,
                                     velocidade, resistencia, tipo)
        self.__lista_personagens.append(personagem_novo)
        return personagem_novo

    def inclui_carta_no_baralho(self, personagem: Personagem) -> Carta:
        carta_nova = Carta(personagem)
        if carta_nova not in self.__baralho:
            self.__baralho.append(carta_nova)
            return carta_nova

    def jogada(self, mesa: Mesa) -> Jogador:
        carta_jogador1 = mesa.carta_jogador1
        carta_jogador2 = mesa.carta_jogador2
        valor_jogador1 = carta_jogador1.valor_total_carta()
        valor_jogador2 = carta_jogador2.valor_total_carta()
        if valor_jogador1 > valor_jogador2:
            mesa.jogador1.inclui_carta_na_mao(carta_jogador1)
            mesa.jogador1.inclui_carta_na_mao(carta_jogador2)
        elif valor_jogador2 > valor_jogador1:
            mesa.jogador2.inclui_carta_na_mao(carta_jogador1)
            mesa.jogador2.inclui_carta_na_mao(carta_jogador2)
        else:
            mesa.jogador1.inclui_carta_na_mao(carta_jogador1)
            mesa.jogador2.inclui_carta_na_mao(carta_jogador2)
        if not mesa.jogador1.mao:
            return mesa.jogador2
        elif not mesa.jogador2.mao:
            return mesa.jogador1
        else:
            return None
