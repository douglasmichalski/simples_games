#!/usr/bin/python

import random

print "Hello! Go play Even or Odd?"

def texto_jogador(x):
	if x == 0:
		return "PAR"
	elif x == 1:
		return "IMPAR"

def texto_maquina(x):
	if x == 0:
		return "IMPAR"
	elif x == 1:
		return "PAR"	

def check_winner(num_player, player):
	num_machine = random.randint(0, 10)
	is_even = 0	

	if ((num_player + num_machine % 2) != 0): is_even = 1
	
	if (is_even == 1 and player == 0):
		print "\nParabens voce ganhou :D a maquina escolheu %d" % (num_machine)
	else: 
		print "\nVoce perdeu :( pois a maquina escolheu %d" % (num_machine)
	return "";

#Primeiro perguntar ao jogador se ele quer ser par ou impar
jogador = input("Digite: (0) => PAR ou (1) => IMPAR: ")

while (jogador != 0 and jogador != 1):
	print ("Escolha incorreta, vamos tentar novamente")
	jogador = input("\nEscolha: Par (1) ou Impar (2)? ")

print "\nVoce escolheu %s e seu oponente a maquina ficara com %s" % (texto_jogador(jogador), texto_maquina(jogador))

#Depois receber um numero a escolha do jogador de 0 a 10

numero_jogador = input("\nAgora escolha um numero entre 0 e 10: ")

while (numero_jogador < 0 or numero_jogador > 10):
	numero_jogador = input("Escolha incorreta, escolha um numero entre 0 e 10: ")

#Verificar quem ganhou e imprimir o jogador 
print check_winner(numero_jogador, jogador)





