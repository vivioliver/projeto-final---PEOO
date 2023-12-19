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

    def iniciar_contagem_regressiva(self):
        self.contagem_regressiva = 10
        self.atualizar_contagem_regressiva()

    def atualizar_contagem_regressiva(self):
        self.label_contagem_regressiva.config(text=f"Tempo restante: {self.contagem_regressiva}")
        if self.contagem_regressiva > 0:
            self.contagem_regressiva -= 1
            self.master.after(1000, self.atualizar_contagem_regressiva)
        else:
            self.verificar_resposta()

    def verificar_resposta(self):
        if self.resposta_escolhida == self.pergunta_atual.resposta:
            self.pontuacao += 1
            feedback = "Resposta correta!"
        else:
            feedback = f"Resposta incorreta. A resposta correta é: {self.pergunta_atual.resposta}"

        messagebox.showinfo("Feedback", feedback)
        self.perguntas.remove(self.pergunta_atual)
        self.proxima_pergunta()

    def mostrar_dica(self):
        dica = self.pergunta_atual.dica
        messagebox.showinfo("Dica", dica)

    def mostrar_resultado(self):
        resultado = f"Sua pontuação final: {self.pontuacao}/{len(perguntas)}"
        messagebox.showinfo("Resultado", resultado)
        self.master.destroy()

perguntas = [
    Pergunta("O que um programador faz quando está com fome enquanto codifica?", ["Come bytes de informação", "Faz um lanche rápido", "Pede um delivery de código-fonte", "Niels Bohr"], "Come bytes de informação", "Porque a fome não espera por compilação!"),
    Pergunta("Qual é a comida favorita do programador?", ["Fish and Chips", "Cookies e Cache", "Bits de Frango", "Niels Bohr"], "Cookies e Cache", "Porque é rápido e armazenado para acesso futuro."),
    Pergunta("Qual é o animal favorito do programador?", ["Gato", "Cachorro", "Pinguim", "Niels Bohr"], "Pinguim", "Porque ele gosta de Linux."),
    Pergunta("O que o programador faz antes de dormir?", ["Fecha os olhos", "Desliga o computador", "Fecha a tampa do laptop", "Niels Bohr"], "Fecha a tampa do laptop", "Para entrar no modo de suspensão."),
    Pergunta("Por que o programador odeia ir à praia?", ["Medo de sol", "Problemas com areia", "Não sabe nadar", "Niels Bohr"], "Problemas com areia", "Porque é difícil evitar os bugs na areia."),
    Pergunta("Como o programador pede pizza?", ["Por telefone", "Online", "Usando APIs de entrega", "Niels Bohr"], "Usando APIs de entrega", "Porque ele gosta de pedir com eficiência."),
    Pergunta("O que o programador mais gosta de assistir?", ["Séries de comédia", "Filmes de ação", "Documentários técnicos", "Niels Bohr"], "Documentários técnicos", "Para aprender novas tecnologias."),
    Pergunta("Qual é o superpoder secreto do programador?", ["Voar", "Invisibilidade", "Debugging instantâneo", "Niels Bohr"], "Debugging instantâneo", "Resolver problemas com um único olhar."),
    Pergunta("O que o programador diz para a sua cafeína?", ["Você me deixa acordado", "Você me dá energia", "Você é meu combustível", "Niels Bohr"], "Você é meu combustível", "Porque cafeína é essencial para a codificação!"),
    Pergunta("Se nossa professora de programação fosse uma guru da moda no mundo da codificação, como descreveríamos seu estilo e paleta de cores estilosa?", ["Pixel Prism - reinventando a moda com uma mistura de pixels multicoloridos, capturando a essência da programação criativa.", "Stylish Scripter - deslumbrando com um visual moderno, misturando preto, rosa e detalhes em prata", "Code Couture - brilhando com uma paleta vibrante de verde-limão, roxo e toques de código dourado", "Cyber Chic - reinventando a moda com uma mistura de preto, azul elétrico e detalhes de neon"], "Pixel Prism - reinventando a moda com uma mistura de pixels multicoloridos, capturando a essência da programação criativa.", "Sobre nossa professora Priscilla")
]


root = tk.Tk()
app = QuizApp(root, perguntas)
root.mainloop()