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
        titulo="Sistema de Cadastramento de fornecedores - Menu"
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
            text="Você está no sistema de cadastro de fornecedores da Prefeitura Municipal de Céu Azul,"
                 "para realizar seu cadastro informe os dados cadastrais de sua empresa.",
            wraplength=390,
        )
        self.explicacao_label.pack(pady=30)

        self.explicacao_label = tk.Label(
            tela, 
            text="Caso precise de ajuda para alteração de alguma informação, entre em contato através da opção Suporte.",
            wraplength=400,
        )
        self.explicacao_label.pack(pady=10)

if __name__ == "__main__":
    tela = tk.Tk()
    meumenu = MeuMenu(tela)
    tela.iconbitmap('brasao.ico')
    tela.mainloop()