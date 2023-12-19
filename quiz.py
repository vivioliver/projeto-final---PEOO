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


        
        for i in range(4):
            opcao_radio = tk.Radiobutton(self.master, text="", variable=self.opcoes_var, value="", command=self.selecionar_resposta)
            opcao_radio.pack()
            self.opcoes_radio.append(opcao_radio)

        self.botao_ajuda = tk.Button(self.master, text="Dica", command=self.mostrar_dica)
        self.botao_ajuda.pack(pady=10)

        self.botao_proxima_pergunta = tk.Button(self.master, text="Próxima Pergunta", command=self.proxima_pergunta)
        self.botao_proxima_pergunta.pack(pady=10)

        self.proxima_pergunta()

    def proxima_pergunta(self):
        if self.perguntas:
            self.pergunta_atual = random.choice(self.perguntas)
            self.iniciar_contagem_regressiva()
            self.atualizar_interface()
        else:
            self.mostrar_resultado()

    def atualizar_interface(self):
        self.label_pontuacao.config(text=f"Pontuação: {self.pontuacao}")
        self.barra_progresso['value'] = 100
        self.label_contagem_regressiva.config(text="Tempo restante: 10")
        self.label_pergunta.config(text=self.pergunta_atual.pergunta)

        opcoes = self.pergunta_atual.opcoes
        random.shuffle(opcoes)
        
        for i in range(4):
            self.opcoes_radio[i].config(text=opcoes[i], value=opcoes[i])

    def selecionar_resposta(self):
        self.resposta_escolhida = self.opcoes_var.get()