import tkinter as tk
from tkinter import *
import os

class MeuMenu:
    def lrepresentantes(self):
        self.tela.destroy()
        os.system("python interno/lista_representante.py")  

    def lempresas(self):
        self.tela.destroy()
        os.system("python interno/lista_empresa.py")  

    def cadinterno(self):
        self.tela.destroy()
        os.system("python interno/cadastro_interno.py")

    def linterno(self):
        self.tela.destroy()
        os.system("python interno/lista_interno.py") 

    def __init__(self, tela):
        self.tela = tela
        titulo="Sistema de Cadastramento de fornecedores - Menu"
        self.titulo=titulo
        self.tela.title(titulo)
        self.tela.geometry("500x200")
        self.barraDeMenus = Menu(self.tela)
        self.menuFuncoes = Menu(self.barraDeMenus, tearoff=0)
        self.menuFuncoes.add_command(label="Lista Mandatários", command=self.lrepresentantes)
        self.menuFuncoes.add_command(label="Lista Empresas", command=self.lempresas)
        self.menuFuncoes.add_command(label="Cadastro Interno", command=self.cadinterno)
        self.menuFuncoes.add_command(label="Lista Interno", command=self.linterno)
        self.menuFuncoes.add_separator()
        self.menuFuncoes.add_command(label="Sair", command=self.tela.quit)
        self.barraDeMenus.add_cascade(label="Funções", menu=self.menuFuncoes)

        self.tela.config(menu=self.barraDeMenus)

        self.explicacao_label = tk.Label(
            tela, 
            text="Você está no sistema de cadastro de fornecedores da Prefeitura Municipal de Céu Azul,"
                 "aqui você tem acesso aos dados de todos os representantes e empresas cadastrados.",
            wraplength=390,
        )
        self.explicacao_label.pack(pady=30)

        self.explicacao_label = tk.Label(
            tela, 
            text="Sistema desenvolvido por Everton Gabriel Käfer"
                 ,
            wraplength=390,
        )
        self.explicacao_label.pack(pady=10)

if __name__ == "__main__":
    tela = tk.Tk()
    meumenu = MeuMenu(tela)
    tela.iconbitmap('brasao.ico')
    tela.mainloop()