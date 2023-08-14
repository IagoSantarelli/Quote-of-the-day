#Importando bibliotecas
import requests
import json
import time
import tkinter as tk
from tkinter import messagebox

#Declarando link da requisição API
link = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"

#Declarando o horário de início do processamento
inicio = time.time()

#Trazendo a requisição da API declarada como Requisição
requisicao = requests.get(link)

#print(requisicao.json())

#Declarando requisição em formato Json na variavel dicionário
dicionario = requisicao.json()

#Buscando elemento da requisição e declarando em ma variável
texto = dicionario['text']

#Declarando tempo de delay do processamento
fim = time.time() - inicio

#Abrindo a Messagebox para mostras a informação da variável texto com o titulo declarando antes
messagebox.showinfo("Mensagem do dia", texto)

#Printando no terminal o tempo de delay do processamento
print("Demorou {:.2f} segundos".format(fim))