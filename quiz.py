import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import ttk
from PIL import Image, ImageTk
import random

class Pergunta:
    def __init__(self, pergunta, opcoes, resposta, dica):
        self.pergunta = pergunta
        self.opcoes = opcoes
        self.resposta = resposta
        self.dica = dica

class QuizApp:
    def __init__(self, master, perguntas):
        self.master = master
        self.master.title("Quiz Interativo")
        self.perguntas = perguntas
        self.pontuacao = 0
        self.pergunta_atual = None
        self.contagem_regressiva = 10
        self.resposta_escolhida = None

        self.label_pontuacao = tk.Label(self.master, text="Pontuação: 0", font=("Arial", 12))
        self.label_pontuacao.pack(pady=5)

        self.barra_progresso = ttk.Progressbar(self.master, orient="horizontal", length=200, mode="determinate")
        self.barra_progresso.pack(pady=5)

        self.label_contagem_regressiva = tk.Label(self.master, text="Tempo restante: ", font=("Arial", 10))
        self.label_contagem_regressiva.pack(pady=5)

        self.label_pergunta = tk.Label(self.master, text="", font=("Arial", 12))
        self.label_pergunta.pack(pady=10)

        self.opcoes_var = tk.StringVar()
        self.opcoes_radio = []