import tkinter as tk
from tkinter import messagebox
from tkinter import *
import os

class MeuMenu:
    def cadempresa(self):
        messagebox.showinfo("Aviso", "Preencha o cadastro a seguir com todas as informações necessárias.")
        self.tela.destroy()
        os.system("python usuario/cadastro_empresa.py")

    def suporte(self):
        self.tela.destroy()
        os.system("python usuario/suporte.py")  

    def __init__(self, tela):
        self.tela = tela
        titulo="Sistema de Cadastramento de fornecedores - Suporte"
        self.titulo=titulo
        self.tela.title(titulo)
        self.tela.geometry("500x200")
        self.barraDeMenus = Menu(self.tela)
        self.menuFuncoes = Menu(self.barraDeMenus, tearoff=0)
        self.menuFuncoes.add_command(label="Cadastro Empresa", command=self.cadempresa)
        self.menuFuncoes.add_command(label="Suporte", command=self.suporte)
        self.menuFuncoes.add_separator()
        self.menuFuncoes.add_command(label="Sair", command=self.tela.quit)
        self.barraDeMenus.add_cascade(label="Funções", menu=self.menuFuncoes)

        self.tela.config(menu=self.barraDeMenus)

        self.explicacao_label = tk.Label(
            tela, 
            text="Caso voçê queira realizar alguma alteração cadastral de seua empresa ou mandatário,"
                 "entre em contato com o setor de suporte atravez de uma das opções a baixo.",
            wraplength=390,
        )
        self.explicacao_label.pack(pady=20)

        self.explicacao_label = tk.Label(
            tela, 
            text="Telefone: 45 40028922",
            wraplength=300,
        )
        self.explicacao_label.pack(pady=1)

        self.explicacao_label = tk.Label(
            tela, 
            text="Email: suporteceuazul@hotmail.com",
            wraplength=300,
        )
        self.explicacao_label.pack(pady=1)

        self.explicacao_label = tk.Label(
            tela, 
            text="Ou vá diretamente ao paço municipal de Céu Azul",
            wraplength=300,
        )
        self.explicacao_label.pack(pady=1)

if __name__ == "__main__":
    tela = tk.Tk()
    meumenu = MeuMenu(tela)
    tela.iconbitmap('brasao.ico')
    tela.mainloop()